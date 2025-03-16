def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second_half=slow.next
        slow.next=None

        previous=None
        current=second_half
        while current:
            temp=current.next
            current.next=previous
            previous,current=current,temp

        first_half=head
        second_half=previous
        while second_half:
            temp1=first_half.next
            temp2=second_half.next

            first_half.next=second_half
            second_half.next=temp1

            first_half,second_half=temp1,temp2
        