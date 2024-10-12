using System;  


namespace app
{
    
    class Program
    {
        
        public interface Person 
        {
            void DisplayInformation();
        }
        class Student : Person
        {
            protected string name {get; set;}
            protected int studentID {get; set;}
            protected int age {get; set;}

            // Constructor
            public Student (string name, int studentID, int age)
            {
                this.name = name;
                this.studentID = studentID;
                this.age = age;
            }

            public virtual void DisplayInformation()
            {
                Console.WriteLine($"name: {name}");
                Console.WriteLine($"Student ID: {studentID}");
                Console.WriteLine($"Age: {age}");
            }

            public static Tuple<string, int, int> GetPersonInfo(string name, int studentID, int age)
            {
                return Tuple.Create(name, studentID, age);
            }
        
        }
        class CollegeStudent : Student
        {
            protected string major {get; set;}
            protected int StudentAverage {get; set;}

            public CollegeStudent(string major, int StudentAverage, string name, int studentID, int age) : base(name, studentID, age)
            {
                this.major = major;
                this. StudentAverage = StudentAverage;
                this.name = name;
                this.studentID = studentID;
                this.age = age;
            }

            public override void DisplayInformation()
            {
                base.DisplayInformation();
                Console.WriteLine($"Major: {major}");
                Console.WriteLine($"Student Average: {StudentAverage}");
            }

        }   
        
        static void Main(string[] args)
        {
            CollegeStudent collegeStudent = new CollegeStudent("Computer Science", 100, "John Pork", 12345, 21);
            Student student = new Student ("Joe Biden", 34613, 12);
            
            collegeStudent.DisplayInformation();
            Console.WriteLine(); // adding space
            student.DisplayInformation();
            
        }
    }
}