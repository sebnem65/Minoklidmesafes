#minimum oklid mesafesinin hesaplanması
#noktaların tanımlanması
points = [(3, 1), (5, 4)]
#öklid için fonksiyon yazma
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5
    return distance
#mesafelerin hesaplanması
distances = []
for a in range(len(points)):
    for b in range(a+1,len(points)):
        distance = euclideanDistance(points[a], points[b])
        distances.append(distance)
#mesafenin bulunması
min_distance = min(distances)
print("Minimum mesafe:", min_distance)










