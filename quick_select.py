def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def metric(x, y):
            return x*x + y*y
        
        def partition(l, r, pivot): # [l, r] range
            d = distance(*points[pivot])
            points[r], points[pivot] = points[pivot], points[r]
            
            index = l
            for i in range(l, r):
                if distance(*points[i]) < d:
                    points[i], points[index] = points[index], points[i]
                    index += 1
            points[r], points[index] = points[index], points[r]
            
            return index
        
        
        def quick_select(l, r):
            if l == r:
                return 
            pivot = random.randint(l, r)
            
            pivot = partition(l, r, pivot)
            
            if pivot == k - 1:
                return
            elif pivot > k - 1:
                quick_select(l, pivot - 1)
            else:
                quick_select(pivot + 1, r)
                
        quick_select(0, len(points) - 1)
        
        
        return points[:k]
