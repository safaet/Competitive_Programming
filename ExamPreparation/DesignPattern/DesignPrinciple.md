# Design Principles

## General Design Principles
1. **KISS (Keep It Simple, Stupid)**  
   - Systems should be as simple as possible, avoiding unnecessary complexity.

2. **YAGNI (You Aren't Gonna Need It)**  
   - Don't add functionality until it is absolutely necessary.

3. **DRY (Don't Repeat Yourself)**  
   - Avoid duplication of code by abstracting common logic into reusable modules or methods.

4. **Separation of Concerns (SoC)**  
   - Divide a system into distinct sections, each addressing a separate concern or responsibility.

5. **Law of Demeter (LoD)**  
   - A class should only interact with its immediate collaborators, avoiding unnecessary dependencies.

6. **Encapsulate What Varies**  
   - Identify the parts of the system that are likely to change and encapsulate them to isolate the impact of changes.

7. **Favor Composition Over Inheritance**  
   - Prefer using composition (object relationships) to reuse code rather than relying excessively on inheritance.

8. **Program to Interfaces, Not Implementations**  
   - Depend on abstractions (interfaces) rather than concrete implementations to enhance flexibility and scalability.

---

## SOLID Principles (Object-Oriented Design)
1. **Single Responsibility Principle (SRP)**  
   - A class should have only one reason to change.

2. **Open/Closed Principle (OCP)**  
   - Software entities should be open for extension but closed for modification.

3. **Liskov Substitution Principle (LSP)**  
   - Subclasses should be substitutable for their base classes without altering the program's behavior.

4. **Interface Segregation Principle (ISP)**  
   - A class should not be forced to implement interfaces it does not use.

5. **Dependency Inversion Principle (DIP)**  
   - High-level modules should depend on abstractions, not on low-level modules.

---

## GRASP Principles (General Responsibility Assignment Software Patterns)
1. **Information Expert**  
   - Assign responsibility to the class with the most relevant data.

2. **Creator**  
   - A class should be responsible for creating instances of other classes when it logically owns or uses them.

3. **Controller**  
   - Assign responsibility for handling system events to a controller class.

4. **Low Coupling**  
   - Reduce dependencies between classes to make the system more maintainable.

5. **High Cohesion**  
   - Ensure that a class is focused on a single task and has closely related responsibilities.

6. **Polymorphism**  
   - Use polymorphism to handle variations in behavior.

7. **Protected Variations**  
   - Protect the system from changes by encapsulating areas of likely variation.

8. **Indirection**  
   - Use intermediate objects to decouple classes and improve flexibility.

9. **Pure Fabrication**  
   - Create classes that don’t map directly to the domain model but improve design (e.g., utility classes).

---

## Other Common Principles
1. **Minimize Accessibility of Classes and Members**  
   - Restrict access to data and methods as much as possible (e.g., using private, protected modifiers).

2. **Design for Testability**  
   - Structure code in a way that makes it easier to test (e.g., dependency injection).

3. **Use Principle of Least Astonishment**  
   - The behavior of a system should be as intuitive as possible to the user.

4. **Don’t Make Me Think**  
   - Code and design should be self-explanatory and require minimal effort to understand.

5. **Fail Fast**  
   - Detect and handle errors as soon as possible to prevent cascading failures.

6. **Acyclic Dependencies Principle**  
   - Avoid cyclic dependencies between modules or classes.

7. **Common Reuse Principle (CRP)**  
   - Classes that are used together should be packaged together.

8. **Reuse-Release Equivalence Principle (REP)**  
   - Only release a package when it can be reused by others.

9. **Single Level of Abstraction Principle (SLAP)**  
   - Each function or method should operate at a single level of abstraction.

10. **Stable Dependencies Principle (SDP)**  
    - Depend on modules that are less likely to change.

11. **Stable Abstractions Principle (SAP)**  
    - The more stable a module is, the more abstract it should be.
