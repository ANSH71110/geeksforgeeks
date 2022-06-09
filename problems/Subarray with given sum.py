class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        k=0
        sum=0
        lim=len(arr)
        j=0
        while k<lim:
            while j<lim:
                sum+=arr[j]
                if sum==s:
                    l=[]
                    l.append(k+1)
                    l.append(j+1)
                    return l
                elif sum>s:
                    break
                elif sum<s and j==lim-1:
                    return [-1]
                j+=1
            sum-=arr[j]
            sum-=arr[k]
            k+=1
        return [-1]
