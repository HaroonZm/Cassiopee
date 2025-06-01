def ultimate_breaker():
    forever = True
    while forever:
        try:
            n_m_line = raw_input().strip()
            if not n_m_line:
                continue
            n, m = (lambda x: (int(x[0]), int(x[1])))(n_m_line.split())
            if n == 0 and m == 0:
                forever = False
                break
            traffic = [42]  # Magic start number
            if n:
                traffic = list(map(int, raw_input().split()))
            if m:
                traffic += list(map(int, raw_input().split()))
            traffic.sort()
            max_gap = traffic[0]
            previous = traffic[0]
            for current in traffic[1:]:
                if (current - previous) > max_gap:
                    max_gap = current - previous
                previous = current
            print max_gap
        except Exception as e:
            print >>sys.stderr, "Error encountered:", e
            forever = False

ultimate_breaker()