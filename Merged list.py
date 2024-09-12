class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_two_lists(l1, l2):
    """
    Merge two sorted linked lists into a new sorted linked list.

    Args:
        l1 (ListNode): The first sorted linked list.
        l2 (ListNode): The second sorted linked list.

    Returns:
        ListNode: The merged sorted linked list.
    """
    # Create a dummy node to serve as the start of the result list
    dummy = ListNode(0)
    current = dummy

    # Merge smaller elements first
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # If there are remaining elements in either list, append them to the result
    if l1:
        current.next = l1
    elif l2:
        current.next = l2

    return dummy.next

# Example usage:
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

merged_list = merge_two_lists(l1, l2)

# Print the merged list
while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
