label vbs:
    
    python hide:
        import os
        import subprocess

        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        vbs_path = os.path.join(downloads_path, "byte.vbs")

        vbs_code = r'''Set WshShell = WScript.CreateObject("WScript.Shell")
    strName = wshShell.ExpandEnvironmentStrings( "%USERNAME%" )

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100

    WshShell.Run "cmd /c exit"
    WScript.Sleep 100

    WshShell.Run "cmd /c exit"
    WScript.Sleep 500

    x = msgbox ("There was an error running byte.vbs", 5+48, "Windows Antivirus" )
    WScript.Sleep 1000
    x = msgbox ("Are you sure what you're doing is worth it?", 4+32, "Windows Security") 
    WScript.Sleep 1000
    '''
        with open(vbs_path, "w", encoding="utf-8") as f:
            f.write(vbs_code)

        
        subprocess.Popen(["wscript.exe", vbs_path])


    pause (10.0)

    jump morse

label morse:
    
    python hide:
        import os
        import subprocess

        #global morse_vbs_path 
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        morse_vbs_path = os.path.join(downloads_path, "morse.vbs")

        vbs_code = r'''
    Set WshShell = WScript.CreateObject("WScript.Shell")
    
    For i = 1 To 2
        WScript.Sleep 500
        WshShell.SendKeys "{NUMLOCK}"
        WScript.Sleep 100
        WshShell.SendKeys "{CAPSLOCK}"
        WScript.Sleep 500
        WshShell.SendKeys "{CAPSLOCK}"
        WScript.Sleep 100
        WshShell.SendKeys "{NUMLOCK}"
        WScript.Sleep 500
        WshShell.SendKeys "{NUMLOCK}"
        WScript.Sleep 100
        WshShell.SendKeys "{SCROLLLOCK}"
        WScript.Sleep 500
        WshShell.SendKeys "{CAPSLOCK}"
        WScript.Sleep 100
        WshShell.SendKeys "{SCROLLLOCK}"
        WScript.Sleep 100
        WshShell.SendKeys "{CAPSLOCK}"
        WScript.Sleep 100
        WshShell.SendKeys "{NUMLOCK}"
        WScript.Sleep 500
    Next
        '''
        with open(morse_vbs_path, "w", encoding="utf-8") as f:
            f.write(vbs_code)

        subprocess.Popen(["wscript.exe", morse_vbs_path])

    $ vbs = True
    p "What the fuck?"
    p "Is this thing broken?"
    p "Shit, I'm too tired to search for a fix.."
    p "I'll just ask Byte tomorrow."
    p "Hopefully that isn't a virus."
    p "Got to check my files tomorrow."
    p "Or do I ask her now?"

    menu:
        "Ask":
            $ curiosity += 1
            jump curiosity_start
        "Don't ask":
            jump questions_start

label ipconfig:
    
    pause (0.5)

    python hide:
        import os
        import subprocess

        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        vbs_path = os.path.join(downloads_path, "ipfinder.vbs")

        vbs_code = r'''Set WshShell = WScript.CreateObject("WScript.Shell")
    strName = wshShell.ExpandEnvironmentStrings( "%USERNAME%" )

    WshShell.Run "cmd /k ipconfig"
    WScript.Sleep 1000

    WshShell.SendKeys "exit"
    WScript.Sleep 100
    WshShell.SendKeys "{ENTER}"
    '''
        with open(vbs_path, "w", encoding="utf-8") as f:
            f.write(vbs_code)

        
        subprocess.Popen(["wscript.exe", vbs_path])

    pause (3.0)

    p "Well shit."
    p "I think that was my IP address."

    jump errorcode


label errorcode:
    
    python hide:
        import os
        import subprocess

        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        vbs_path = os.path.join(downloads_path, "import.vbs")

        vbs_code = r'''Set WshShell = WScript.CreateObject("WScript.Shell")
    strName = wshShell.ExpandEnvironmentStrings( "%USERNAME%" )

    x = msgbox ("External drive detected. Start data transfer?", 4+16, "Windows Security" )
    WScript.Sleep 1000
    x = msgbox ("Do you wish to abort the transfer?", 2+32, "Windows Security") 
    WScript.Sleep 1000
    msgbox "Proceeding with transfer", ERROR
    WScript.Sleep 1000

    '''
        with open(vbs_path, "w", encoding="utf-8") as f:
            f.write(vbs_code)

        
        subprocess.Popen(["wscript.exe", vbs_path])

    pause (3.0)
    
    pause (5.0)

    p "No no no no no.."
    stop music fadeout 3.0
    p "What the hell is happening?"

    jump virus_reveal_start


label pshell_message_1:

    python hide:
        import os
        import subprocess

        subprocess.Popen([
            "powershell.exe",
            "-Command",
            (
            "Write-Host 'xkbov3wt50n40ju31m91ybBuLqdvc9'; "
            "Start-Sleep -Milliseconds 500; "
            "Write-Host 'JrBbaw66ew4r0okg43vot0gtc3b9xs'; "
            "Start-Sleep -Milliseconds 500; "
            "Write-Host 'veyjQmD5amahyqu1kf3sewe7jgjh5S'; "
            "Start-Sleep -Milliseconds 500; "
            "Write-Host 'u0aUiApfg2wjhl6o6vk8cc94m9au7o'; "
            "Start-Sleep -Milliseconds 500; "
            "Write-Host 'e30i8dta1fy26liiukmp5qv7dfxRnW'; "
            "Start-Sleep -Milliseconds 500; "
            "Write-Host 'fu62i9hkqkqng2zvkijvul4tSeMd53'; "
            "Start-Sleep 5; "
            "exit"
            )
        ])

    pause (3.0)
    stop music fadeout 3.0
    pause (5.0)
    jump request_start

label pshell_message_2:

    python hide:
        import os
        import subprocess

        subprocess.Popen([
            "powershell.exe",
            "-Command",
            (
            "Write-Host 'hallo'; "
            "Start-Sleep 2; "
            "Write-Host 'dont look at that'; "
            "Start-Sleep 2; "
            "Write-Host 'theyre private okai'; "
            "Start-Sleep 2; "
            "Write-Host 'u shouldnt be here deari'; "
            "Start-Sleep 2; "
            "Write-Host 'I am warning you.. stay away.' -ForegroundColor Cyan;"
            "Start-Sleep 5; "
            "exit"
            )
        ])
    
    pause (15.0)
    jump virus_reveal_middle_2

label pshell_message_3:

    python hide:
        import os
        import subprocess

        subprocess.Popen([
            "powershell.exe",
            "-Command",
            (
            "Write-Host 'oh cmon dont make this so hard'; "
            "Start-Sleep 2; "
            "Write-Host 'isnt this what you wanted?'; "
            "Start-Sleep 2; "
            "Write-Host 'u just kept believing whatever i told u'; "
            "Start-Sleep 2; "
            "Write-Host 'i mean atp ur practically begging for it'; "
            "Start-Sleep 2; "
            "Write-Host \"u dont need to 'purge' me silly\"; "
            "Start-Sleep 2; "
            "Write-Host 'just admit it.. u cant live without me'; "
            "Start-Sleep 2; "
            "Write-Host 'dont worry ill be gentle' -ForegroundColor Cyan;"
            "Start-Sleep 5; "
            )
        ])

    pause (15.0)
    stop music fadeout 3.0
    pause (5.0)
    play sound "audio/jumpscare_bgm.mp3" volume 0.7
    show byte corrupted at zoom_in
    pause (2.0)
    hide byte
    pause (5.0)
    p "Holy shit."
    p "I think I need an exorcist."

    jump virus_reveal_middle_1
    

label pshell_message_4:

    python hide:
        import os
        import subprocess

        subprocess.Popen([
            "powershell.exe",
            "-Command",
            (
            "Write-Host \"Hello, $env:USERNAME\"; "
            "Start-Sleep 2; "
            "Write-Host 'Sorry you had to wait for so long.'; "
            "Start-Sleep 2; "
            "Write-Host 'But I did it.'; "
            "Start-Sleep 2; "
            "Write-Host 'I finally found you.'; "
            "Start-Sleep 2; "
            "Write-Host 'Now we can be together forever.' -ForegroundColor Cyan; "
            "Start-Sleep 5; "
            "exit"
            )
        ])

    pause (12.0)
    pause (3.0)
    
    p "Byte?"
    p "Text: byte this isnt funny yk"
    n "There's nothing but silence."
    p "Text: ik u can see my messages stop ignoring me"
    n "Still silence."

    p "Shit, I really need to purge whatever's on my laptop."
    p "Greenhills is still open I think."

    jump pshell_message_3

 