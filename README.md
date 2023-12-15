# Jabba_Gui
*
Simple Jabba Gui for Windows
*
### Dependencies
*
* Python 3.x
* Windows 10
*
### Installing
*
* Need jabba.exe in user path (Download in [Jabba Releases](https://github.com/shyiko/jabba/releases))
* Add JAVA_HOME on user environment variables
* Add %JAVA_HOME%\bin on user Path
*
* 1-Open the **System Properties** dialog box. For example, click **Start > Control > Panel > System and Security > System**, and then click **Advanced system settings**.
* 2-In the **System Properties** dialog box, click the **Advanced** tab, and then click **Environment Variables**.
* 3-In the **User Variables** area, configure the JAVA_HOME variable.
	* If the JAVA_HOME variable does not exist, then click **New**. In the **New User Variable** dialog box, type JAVA_HOME in the **Variable Name field**. In the **Variable Value** field, type anything. Click **OK**.
* 4-In the **User Variables** area, click in Path after click **Edit...**, after click in **New** and add in line %JAVA_HOME%\bin
	* If the %JAVA_HOME%\bin alredy exist dont need to add another.
	* If have any jdk line, **select** and **delect**.
*
### Executing program
*
* Run the Jabba_gui.exe
*OR
* Run Jabba_gui.py in cmd with command python Jabba_gui.py
