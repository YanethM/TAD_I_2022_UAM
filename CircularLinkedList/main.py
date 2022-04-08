from circular_linked_list import CircularLinkedList
inst_cll = CircularLinkedList()
inst_cll.prepend('A')
inst_cll.prepend('1')
inst_cll.prepend('2')
inst_cll.prepend('3')
inst_cll.prepend('6')
inst_cll.append('Z')
print('Lista inicial')
inst_cll.show_circular_linked_list()
inst_cll.shift()
inst_cll.pop()
print('Lista después de eliminar el primer y el último nodo')
inst_cll.show_circular_linked_list()


