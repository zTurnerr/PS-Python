# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1.reverse()
        l2.reverse()
        temp1 = 0
        temp2 = 0
        for i in range(len(l1)):
            temp1 += pow(10, i) * l1[i]
        for i in range(len(l2)):
            temp2 += pow(10, i) * l2[i]
        
        ans = temp1 + temp2
        ans_arr = []
        for i in str(ans):
            ans_arr.insert(0,int(i))
        return ans_arr


x = Solution()

print(x.addTwoNumbers([2,4,3], [5,6,4]))
        


    