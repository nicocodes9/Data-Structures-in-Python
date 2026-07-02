# Data-Structures-in-Python
A personal repository dedicated to mastering Data Structures and Algorithms. Includes hands-on code implementations, experimental sandboxes, and detailed notes—with a special deep dive into Linked Lists and memory management.
---

# Data Structures in Python

A curated collection of **classic data structures implemented in Python**. This repository is designed for learners, interview preparation, and developers who want clean, well-documented implementations of fundamental data structures.

---

## 📚 Overview

This project covers a wide range of data structures, each implemented from scratch in Python with clarity and modularity in mind. The goal is to help you:

- Understand **core concepts** behind data structures.
- Learn **Pythonic implementations** of algorithms.
- Practice **time complexity analysis** and usage examples.

---

## 🗂️ Repository Structure

| **Data Structure** | **Description** |
|-----------------------------|-------------------------------|
| **Array** | Fixed-size sequential collection with indexing operations. |
| **Linked List** | Nodes connected via pointers; includes singly & doubly linked lists. |
| **Stack** | LIFO structure with push/pop operations. |
| **Queue** | FIFO structure with enqueue/dequeue. Includes circular and priority queues. |
| **Hash Table** | Key-value mapping with collision handling. |
| **Binary Tree** | Hierarchical structure with traversal methods (DFS, BFS). |
| **Binary Search Tree** | Ordered tree supporting efficient search, insert, delete. |
| **Graph** | Adjacency list/matrix representation with traversal algorithms. |
| **Heap** | Complete binary tree supporting priority queue operations. |

---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/nicocodes9/Data-Structures-in-Python.git
cd Data-Structures-in-Python
```

Run any module directly:

```bash
python linked_list.py
```

---

## 🚀 Usage Examples

### Linked List
```python
from linked_list import LinkedList

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.display()  # Output: 10 -> 20
```

### Stack
```python
from stack import Stack

s = Stack()
s.push(5)
s.push(10)
print(s.pop())  # Output: 10
```

---

## 📊 Complexity Analysis

Each implementation includes **time and space complexity notes**:

- **Array**: Access O(1), Insert O(n)
- **Linked List**: Insert O(1), Search O(n)
- **Stack/Queue**: Push/Pop O(1)
- **Hash Table**: Average O(1), Worst O(n)
- **Binary Search Tree**: Search O(log n) average, O(n) worst
- **Graph Traversal**: O(V + E)

---

## 🧩 Contribution Guidelines

- Fork the repo and create a new branch.
- Add new data structures or improve existing ones.
- Ensure code is **PEP8 compliant** and includes **docstrings**.
- Submit a pull request with clear commit messages.

---

## 🎯 Roadmap

- Add **advanced trees** (AVL, Red-Black).
- Implement **graph algorithms** (Dijkstra, Kruskal, Prim).
- Provide **unit tests** for all structures.
- Expand with **real-world use cases**.

---

## 📜 License

This project is licensed under the MIT License — free to use, modify, and distribute.

