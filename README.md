# Online Examination System 📝🎓

A comprehensive, role-based console portal built in Python using core **Object-Oriented Programming (OOP)** principles. This application simulates a live test engine environment, establishing secure execution scopes between Teacher dashboards (exam creation & provisioning) and Student workspaces (live test evaluations & dynamic report cards).

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML).
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Learning Data Structures & Algorithms (DSA) and data science libraries like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Role-Based Access Control:** Separate conditional workflows mapped uniquely for `Student` interactions and `Teacher` authority paths derived from a unified authentication core.
*   **Dynamic Exam Creator Engine:** Allows teachers to instantly define unique test configurations (`Exam ID`, `Title`, `Duration`) and seed custom multi-choice questionnaires.
*   **Interactive Testing Portal:** Features live input listeners checking integer answers dynamically against hidden correct key references, complete with countdown-delay styling (`time.sleep`).
*   **Instant Result Matrix & Grading:** Dynamically calculates total marks upon submission, flags structural grading profiles (`Pass` / `Fail` benchmarks set at 50%), and maintains an ongoing past results report card ledger.
*   **Pre-Configured Mock Environments:** Populates pre-loaded mock profiles (Prof. Vishal Sharma & Student Krishna) out-of-the-box for instant platform testing.

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This enterprise-inspired project relies heavily on decoupled object layers:
*   **Inheritance Hierarchy:** Implements clean class structures where specialized classes `Student` and `Teacher` reuse parameters from the central `User` super-class through `super().__init__()`.
*   **Deep Composition & Relational Mapping:** The master management controller class (`OnlineExamSystem`) controls an internal relational matrix map containing active `User` objects and lists of distinct `Exam` blueprints, which recursively hold arrays of independent `Question` nodes.
*   **Type Evaluation & Polymorphic Logic:** Leverages native type-checking constraints (`isinstance()`) to route system users down distinct graphical workflow dashboards automatically based on their structural object definition.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd online-examination-system-oop
    ```
3.  **Run the core terminal engine:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   Python 3.x installed on your machine.
