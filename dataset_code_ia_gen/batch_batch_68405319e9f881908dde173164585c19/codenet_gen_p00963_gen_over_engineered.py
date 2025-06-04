import math
from abc import ABC, abstractmethod
from typing import Tuple, Dict, List, Optional

# Constants for vertices
class Vertex:
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'

# Represents an immutable Edge between two vertices, unordered
class Edge:
    def __init__(self, v1: str, v2: str):
        if v1 == v2:
            raise ValueError("Edge endpoints must be distinct")
        self.vs = tuple(sorted((v1, v2)))

    def __eq__(self, other):
        return isinstance(other, Edge) and self.vs == other.vs

    def __hash__(self):
        return hash(self.vs)

    def __repr__(self):
        return f"{self.vs[0]}{self.vs[1]}"

# Represents a Face of the tetrahedron, identified by its 3 vertices, sorted
class Face:
    def __init__(self, v1: str, v2: str, v3: str):
        vertices = sorted((v1, v2, v3))
        if len(set(vertices)) != 3:
            raise ValueError("Face must have three distinct vertices")
        self.vs = tuple(vertices)

    def __eq__(self, other):
        return isinstance(other, Face) and self.vs == other.vs

    def __hash__(self):
        return hash(self.vs)

    def __repr__(self):
        return f"Face{''.join(self.vs)}"

    def contains_vertex(self, v: str) -> bool:
        return v in self.vs

    def contains_edge(self, e: Edge) -> bool:
        return e.vs[0] in self.vs and e.vs[1] in self.vs

# Abstract class for a Worm's path on faces and edges
class WormPath(ABC):

    @abstractmethod
    def position(self) -> Tuple[Face, Tuple[float, float]]:
        """
        Returns the face where the worm stopped, and the local 2D coordinates of the position.
        Coordinates parametrized on the face, unit edge length basis.
        """
        pass

# Concrete class for the regular tetrahedron geometry and path computations
class TetrahedronGeometry:
    def __init__(self):
        # Define vertices for the regular tetrahedron in 3D space, for vector computations
        self.vertices_3d = {
            Vertex.A: (1, 1, 1),
            Vertex.B: (1, -1, -1),
            Vertex.C: (-1, 1, -1),
            Vertex.D: (-1, -1, 1)
        }
        self.edges = set([
            Edge(Vertex.A, Vertex.B),
            Edge(Vertex.A, Vertex.C),
            Edge(Vertex.A, Vertex.D),
            Edge(Vertex.B, Vertex.C),
            Edge(Vertex.B, Vertex.D),
            Edge(Vertex.C, Vertex.D)
        ])
        # Faces as sets of vertices
        self.faces = [
            Face(Vertex.A, Vertex.B, Vertex.C),
            Face(Vertex.A, Vertex.B, Vertex.D),
            Face(Vertex.A, Vertex.C, Vertex.D),
            Face(Vertex.B, Vertex.C, Vertex.D),
        ]
        # Map from unordered edge to adjacent faces (exactly 2)
        self.edge_to_faces: Dict[Edge, List[Face]] = {}
        for e in self.edges:
            self.edge_to_faces[e] = []
            for f in self.faces:
                if f.contains_edge(e):
                    self.edge_to_faces[e].append(f)
        # Check validity: each edge belongs to exactly two faces
        for e, flist in self.edge_to_faces.items():
            if len(flist) != 2:
                raise ValueError(f"Edge {e} does not belong to exactly two faces")

        # Precompute orthonormal coordinate basis for each face: used for 2D parametrization and angles
        # For each face, store tuple (origin=vertexA in face, vector_u, vector_v) defining 2D coords in plane
        self.face_bases: Dict[Face, Tuple[Tuple[float,float,float], Tuple[float,float,float], Tuple[float,float,float]]] = {}
        for f in self.faces:
            # Pick vertex with smallest alphabetical order as origin for face plane 2D coords
            sorted_vs = sorted(f.vs)
            origin = self.vertices_3d[sorted_vs[0]]
            v1 = self.vertices_3d[sorted_vs[1]]
            v2 = self.vertices_3d[sorted_vs[2]]
            # Basis vectors in face plane (v1-origin) and (v2-origin)
            u_raw = vector_sub(v1, origin)
            v_raw = vector_sub(v2, origin)
            # Normalize u_raw to unit length
            u = normalize(u_raw)
            # Project v_raw to plane orthogonal to u
            v_proj = vector_sub(v_raw, scalar_mult(u, dot(v_raw, u)))
            v = normalize(v_proj)
            self.face_bases[f] = (origin, u, v)

    def get_face_opposite_vertex(self, vertex: str) -> Face:
        # The face opposite to a vertex is the one not containing that vertex
        for f in self.faces:
            if vertex not in f.vs:
                return f
        raise ValueError(f"No face opposite to vertex {vertex}")

    def get_face_from_vertices(self, v1: str, v2: str, v3: str) -> Face:
        return Face(v1, v2, v3)

    def get_opposite_vertex_of_edge_in_face(self, edge: Edge, face: Face) -> str:
        # face has 3 vertices - edge has 2 - the remaining vertex in face is opposite vertex on face to edge
        for v in face.vs:
            if v not in edge.vs:
                return v
        raise ValueError(f"Face {face} does not contain vertices outside edge {edge}")

    def face_frame_to_3d(self, face: Face, u_coord: float, v_coord: float) -> Tuple[float, float, float]:
        # Map 2D coordinates in face to 3D coordinates
        origin, u, v = self.face_bases[face]
        p = vector_add(origin, vector_add(scalar_mult(u,u_coord), scalar_mult(v,v_coord)))
        return p

    def vector_angle_deg(self, v1: Tuple[float,float,float], v2: Tuple[float,float,float]) -> float:
        # Returns angle between vectors in degrees
        a = normalize(v1)
        b = normalize(v2)
        c = dot(a,b)
        c = max(min(c,1.0), -1.0)
        return math.degrees(math.acos(c))

    def vector_rotate_around_axis(self, v: Tuple[float,float,float], axis: Tuple[float,float,float], angle_deg: float) -> Tuple[float,float,float]:
        # Rodrigues' rotation formula to rotate v in 3D around unit vector axis by angle in degrees
        angle = math.radians(angle_deg)
        k = normalize(axis)
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        v_rot = vector_add(
            scalar_mult(v, cos_theta),
            vector_add(
                scalar_mult(cross(k, v), sin_theta),
                scalar_mult(k, dot(k,v)*(1-cos_theta))
            )
        )
        return v_rot

# Vector utilities
def vector_sub(a, b):
    return tuple(x - y for x,y in zip(a,b))

def vector_add(a, b):
    return tuple(x + y for x,y in zip(a,b))

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def length(v):
    return math.sqrt(dot(v,v))

def normalize(v):
    l = length(v)
    if l == 0:
        raise ValueError("Zero length vector")
    return tuple(x/l for x in v)

def angle_between_vectors_deg(u, v):
    return math.degrees(math.acos(max(min(dot(normalize(u), normalize(v)),1),-1)))

# WormDirection abstracts the initial direction across the first crossed edge on initial face
class WormDirection:
    def __init__(self, tetra: TetrahedronGeometry,
                 first_edge_str: str,
                 angle_deg: int):
        """
        first_edge_str: like 'BC', 'CD', 'DB', unordered edge crossed first
        angle_deg: angle in degrees (1 to 59) between edge AX and worm's initial direction in face AX Y
        """
        # Parse first edge vertices
        e_vertices = tuple(first_edge_str)
        if len(e_vertices) != 2 or set(e_vertices) - {'B','C','D'}:
            raise ValueError(f"Invalid first edge string: {first_edge_str}")
        # The first face is triangle AXY (A + first_edge vertices)
        vX, vY = e_vertices
        self.first_edge = Edge(vX, vY)
        self.angle_deg = angle_deg
        self.tetra = tetra

        # Determine first face = Face(A, X, Y)
        self.first_face = tetra.get_face_from_vertices(Vertex.A, vX, vY)
        # Point A coords
        A3d = tetra.vertices_3d[Vertex.A]
        X3d = tetra.vertices_3d[vX]
        Y3d = tetra.vertices_3d[vY]

        # Compute initial direction vector on first face:
        # Reference direction is edge A X
        # We rotate edge A X around axis perpendicular to face AXY (vertex order A,X,Y) by angle_deg towards edge A Y
        # Find plane normal via cross(A->X, A->Y)
        vecAX = vector_sub(X3d, A3d)
        vecAY = vector_sub(Y3d, A3d)
        normal = normalize(cross(vecAX, vecAY))

        # To find the sign (direction of rotation) toward AY from AX, we check if cross(AX, dir) has positive component on normal. Rotate AX by angle_deg towards AY.
        # Angle between AX and AY < 60° actually (equilateral)
        # Since worm's angle d is the smaller angle between AX and worm direction measured inside face triangle, rotation is from AX towards AY inside plane.

        # Let's compute base angle AX->AY in degrees for sanity (should be 60°)
        base_angle = angle_between_vectors_deg(vecAX, vecAY)
        if not (59.9 < base_angle < 60.1):
            # numerical safety, tetrahedron equilateral edges have 60° angles on faces
            pass

        # Compute rotation direction: positive rotation around normal to bring AX to AY
        # We express worm vector as rotating AX by +d degrees toward AY inside the face plane, so rotation axis is normal
        self.initial_direction = tetra.vector_rotate_around_axis(vecAX, normal, angle_deg)

        # Normalize direction projected in face plane (should be unit vector)
        self.initial_direction = normalize(self.initial_direction)

# Worm crawl simulation on the tetrahedron surface
class WormSimulator(WormPath):
    def __init__(self, tetra: TetrahedronGeometry,
                 first_edge_str: str,
                 angle_deg: int,
                 trail_length: int):
        self.tetra = tetra
        self.first_edge_str = first_edge_str
        self.angle_deg = angle_deg
        self.trail_length = trail_length
        self.direction = WormDirection(tetra, first_edge_str, angle_deg)
        # The worm starts at vertex A on face AxY (A + edge vertices)
        self.current_face = self.direction.first_face
        self.position_on_face = (0.0,0.0) # At vertex A in face coords, we will parametrize position as (dist to A along base vectors)
        # The initial position in 2D coords of the face is origin at vertex A (0,0)
        # The initial direction vector in 3D is self.direction.initial_direction

    def simulate(self) -> Tuple[Face, Tuple[float, float]]:
        """
        Simulate the worm crawling on the tetrahedron surface starting at vertex A on initial face,
        with initial 3D direction vector.

        The worm moves straight ahead on the current face until it hits an edge,
        then crosses to the adjacent face, preserving the angle of crossing relative to the crossed edge.

        The worm stops after travelling trail_length units along the surface (edges have unit length).
        Because the trail length is an integer and the problem introduces tolerances, we can simulate stepwise.

        Returns the final face and 2D position (local face coordinates) of the worm's stop point.
        """
        total_len = self.trail_length
        pos2d = (0.0, 0.0)
        face = self.current_face
        dir3d = self.direction.initial_direction
        traveled = 0.0

        # Utility to get 2D direction vector on face plane from 3D direction vector
        def project_dir_to_face_2d(face: Face, dir3d: Tuple[float,float,float]) -> Tuple[float,float]:
            origin, u, v = self.tetra.face_bases[face]
            # dir3d projected onto plane(u,v) basis: (u·dir3d, v·dir3d)
            return (dot(dir3d,u), dot(dir3d,v))

        # Utility to find intersection distance along direction until edge is hit on current face
        # The face is triangle (A,X,Y) with local 2D coords
        # Current position pos2d, direction vector 2ddir
        # Need to find minimal positive t>0 such that pos2d + t*2ddir intersects triangle edge (except the one facing back to starting vertex)
        # We exclude the vertex A from intersections since worm never stops near vertices except start.
        # The problem states worms are always more than 0.001 distant from edges and vertices at stop.
        # The method is to compute intersection with each edge segment.
        def find_edge_intersection(face: Face, pos2d: Tuple[float,float], dir2d: Tuple[float,float]) -> Tuple[float, Edge]:
            # face vertices in 2D coords: A(0,0), B at u=1,0 or v=1? The base is arbitrary but unit length edges
            # Actually, on face_AXY, the edge lengths are unit.
            # The base is set such that origin = A, u = vector to first other vertex, v = vector to second other vertex orthogonal in plane
            # The vertices in 2D coordinates are:
            origin, u, v = self.tetra.face_bases[face]
            vA = (0.0,0.0)
            # Vertices in face.vs sorted: e.g., (A,B,C)
            sorted_vs = sorted(face.vs)
            # The base origin is sorted_vs[0]
            # We know that face.vs contains A always except for the last face
            # For faces containing A, origin = A, u points toward second vertex, v points toward third vertex orthogonalized
            # We identify B and C:
            # Get the 2 other vertices in face besides origin:
            other_vertices = [vtx for vtx in sorted_vs if vtx != origin]
            B = other_vertices[0]
            C = other_vertices[1]
            # Positions 3d:
            pB3d = self.tetra.vertices_3d[B]
            pC3d = self.tetra.vertices_3d[C]
            # 2D coords of B and C:
            pB_2d = (dot(vector_sub(pB3d, origin), u), dot(vector_sub(pB3d, origin), v))
            pC_2d = (dot(vector_sub(pC3d, origin), u), dot(vector_sub(pC3d, origin), v))

            vertices_2d = [vA, pB_2d, pC_2d]
            edges_2d = [
                (vA, pB_2d, Edge(origin, B)),
                (vA, pC_2d, Edge(origin, C)),
                (pB_2d, pC_2d, Edge(B, C))
            ]

            t_candidates = []
            for (p1, p2, edge) in edges_2d:
                # Skip if edge contains origin and pos2d is at origin => to avoid immediate edge intersection at start
                # But simpler: calculate intersection anyway, limit to t > 1e-9 to avoid zero or negative

                intersect = line_ray_segment_intersection(pos2d, dir2d, p1, p2)
                if intersect is not None:
                    t, s = intersect
                    if t > 1e-9 and 0 <= s <= 1:
                        t_candidates.append( (t, edge) )

            if not t_candidates:
                # No intersections found, should not happen for correct worm path
                raise RuntimeError("No edge intersection found")
            # Return minimal positive t and corresponding edge
            t_min, edge_min = min(t_candidates, key=lambda x: x[0])
            return t_min, edge_min

        # Helper: find intersection of ray pos2d + t*dir2d (t>=0)
        # with segment (p1,p2), return (t,s) with s parameter along segment, or None if no intersection
        def line_ray_segment_intersection(ray_origin, ray_dir, seg_p1, seg_p2) -> Optional[Tuple[float,float]]:
            # Solve for t,s where:
            # ray_origin + t*ray_dir = seg_p1 + s*(seg_p2 - seg_p1), with t>=0, s in [0,1]
            dx = seg_p2[0] - seg_p1[0]
            dy = seg_p2[1] - seg_p1[1]
            A = [[ray_dir[0], -dx],
                 [ray_dir[1], -dy]]
            b = [seg_p1[0]-ray_origin[0],
                 seg_p1[1]-ray_origin[1]]
            det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
            if abs(det) < 1e-14:
                return None
            t = (b[0]*A[1][1]-b[1]*A[0][1])/det
            s = (A[0][0]*b[1] - A[1][0]*b[0])/det
            if t < 0 or s < 0 or s > 1:
                return None
            return (t, s)

        while traveled < total_len:
            # Project current 3D direction into face