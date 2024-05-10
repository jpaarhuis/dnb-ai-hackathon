using System;

namespace BadCodeExample
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 10, y = 20;
            var manager = new Manager();
            manager.DoSomething(x, y);
            Console.WriteLine("End of program");
            Console.ReadKey();
        }
    }

    class Manager
    {
        public void DoSomething(int a, int b)
        {
            DatabaseStuff(a, b);
        }

        private void DatabaseStuff(int param1, int param2)
        {
            var util = new Utility();
            var result = param1 + param2;
            Console.WriteLine("Processing data...");
            util.ProcessData(result, "hardcoded string");
        }
    }

    class Utility
    {
        public void ProcessData(int data, string info)
        {
            if (data > 1000)
            {
                Console.WriteLine("Big number");
            }
            else if (data < -1000)
            {
                Console.WriteLine("Negative number");
            }

            string path = "C:\\Users\\HardcodedPath";
            Console.WriteLine("Info: " + info);
        }
    }
}