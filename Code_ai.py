Imports System.Diagnostics

Module Module1
    Sub Main()
        Dim pythonExePath As String = "C:\path\to\python.exe" ' Update this path to the location of your Python executable
        Dim pythonScriptPath As String = "C:\path\to\ai_script.py" ' Update this path to the location of your Python script

        Dim process As New Process()
        process.StartInfo.FileName = pythonExePath
        process.StartInfo.Arguments = pythonScriptPath
        process.StartInfo.UseShellExecute = False
        process.StartInfo.RedirectStandardOutput = True
        process.StartInfo.RedirectStandardError = True
        process.StartInfo.CreateNoWindow = True
        process.Start()

        Dim output As String = process.StandardOutput.ReadToEnd()
        Dim errors As String = process.StandardError.ReadToEnd()
        process.WaitForExit()

        Console.WriteLine("Output: " & output)
        Console.WriteLine("Errors: " & errors)
    End Sub
End Module
