using System;
using System.Collections.Generic;
using System.IO;

namespace TvRenamer
{
    class Program
    {
        static void Main(string[] args)
        {
            var files = new List<string> { };
            var type = "";
            foreach (string f in Directory.EnumerateFiles(".")) {
                if (f.EndsWith(".mp4"))
                {
                    files.Add(f);
                    type = "mp4";
                }

                if (f.EndsWith(".mkv"))
                {
                    files.Add(f);
                    type = "mkv";
                }
            }

            Console.WriteLine("Please enter the name of the show");
            string show = Console.ReadLine();
            Console.WriteLine("Please enter the season of the show (enter the number as a double digit; i.e. 01)");
            string season = Console.ReadLine();
            Console.WriteLine("Please enter the resolution/Extra info");
            string extra = Console.ReadLine();

            int i = 0;
            foreach (string f in files)
            {
                i++;
                string ep = i.ToString("00");
                File.Move(f, $"{show} - s{season}e{ep} - {extra}.{type}");
            }

        }
    }
}
