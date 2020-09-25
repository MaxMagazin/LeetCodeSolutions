# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        firstNumber = self.getNumber(l1)
        secondNumber = self.getNumber(l2)

        resultSum = firstNumber + secondNumber

        prevNode = None
        firstNode = None
        while True:
            rest = resultSum % 10

            newNode = ListNode()
            newNode.val = rest
            if prevNode is not None:
                prevNode.next = newNode
            else:
                firstNode = newNode
            prevNode = newNode

            if (resultSum - rest) == 0:
                break

            resultSum = int((resultSum - rest) / 10)
            print("resultSum:", resultSum)

        return firstNode

    def getNumber(self, l1: ListNode):
        num = 0
        i = 0
        while True:
            num += l1.val * pow(10, i)
            i += 1
            if l1.next is None:
                break
            l1 = l1.next
        print(num)
        return num


