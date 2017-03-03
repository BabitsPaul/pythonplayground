def slice_polygon(poly, part):
    # find the "corner point"
    last_slice = None
    last_pt = None

    for pt in poly:
        s = [x for x in part if pt in x]

        if s:
            if last_slice in s:
                break

            last_slice = s[0]

        last_pt = pt

    # find slicing starting from border-point
    a = poly.index(last_pt)
    b = (a + 1) % len(poly) # current positions on the polygon
    sliced_poly = []    # current polygon
    slicing = []    # list of all polygons that are created by the slicing
    while a != b:
        if not [x for x in part if poly[a] in x]:
            # point doesn't lie on slicing-line => add to current polygon
            sliced_poly.insert(0, poly[a])             # prepend point
            a = (a - 1 + len(poly)) % len(poly)  # advance a by one
        elif not [x for x in part if poly[b] in x]:
            # point doesn't lie on slicing-line => add to current polygon
            sliced_poly.append(poly[b])                # append point
            b = (b + 1 + len(poly)) % len(poly)  # advance by one
        else:
            # append points of slicing line
            sliced_poly.insert(0, poly[a])
            sliced_poly.append(poly[b])

            # store created polygon and start over
            slicing.append(sliced_poly)
            sliced_poly = []

            # remove partitioning-line at which the algorithm stopped
            part.remove([x for x in part if poly[a] in x and poly[b] in x][0])

    # add last point to the current polygon, as it's not yet added to it
    sliced_poly.append(poly[a])
    # add last polygon to result-set
    slicing.append(sliced_poly)

    return slicing


# test
polygon = [(150, 110), (270, 40), (425, 90), (560, 150), (465, 290), (250, 290), (90, 220)]
partition = [((270, 40), (250, 290)), ((425, 90), (250, 290))]
print(slice_polygon(polygon, partition))
