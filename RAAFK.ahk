#Requires AutoHotkey v2  

; CONFIGURATION
; Keys to press  
keys := ["W", "A", "S", "D", "Space", "I", "O", "Left", "Right"]  

; Key press duration (ms)  
min_press_time := 300  
max_press_time := 2200  

; Delay between each key press (ms)  
min_key_delay := 300  
max_key_delay := 800  

; Delay between complete cycles (ms)  
min_cycle_delay := 1500  
max_cycle_delay := 4000  

; Code loop
Loop  
{  
    ; Multi key press logic, max 3 keys at a time
    if (Random(0, 3) = 0)  
    {   
        num_keys := Random(2, 3)  
        keys_to_press := []  

        ; Select unique keys & check for duplicate keys 
        while (keys_to_press.Length < num_keys)  
        {  
            index := Random(1, keys.Length)  
            key := keys[index]  
  
            already_exists := false  
            for existing_key in keys_to_press  
            {  
                if (existing_key = key)  
                {  
                    already_exists := true  
                    break  
                }  
            }  

            if (!already_exists)  
                keys_to_press.Push(key)  
        }  

        ; Press n release all selected keys randomly
        for key in keys_to_press  
        {  
            Send("{" key " down}")  
        }  

        duration := RandInt(min_press_time, max_press_time)  
        Sleep duration  
  
        for key in keys_to_press  
        {  
            Send("{" key " up}")  
        }  

        ; Random delay before the next cycle  
        cycle_delay := RandInt(min_cycle_delay, max_cycle_delay)  
        Sleep cycle_delay  
    }  
    else  
    {  
        ; Random select single key  
        index := Random(1, keys.Length)  
        current_key := keys[index]  

        ; Press n release keys randomly  
        duration := RandInt(min_press_time, max_press_time)  
        Send("{" current_key " down}")  
        Sleep duration  
        Send("{" current_key " up}")  
  
        key_delay := RandInt(min_key_delay, max_key_delay)  
        Sleep key_delay  

        ; Extra key press for more chaos  
        if (Random(0, 1))  
        {  
            extra_key_index := Random(1, keys.Length)  
            extra_key := keys[extra_key_index]  
            extra_duration := RandInt(100, 400)  
            Send("{" extra_key " down}")  
            Sleep extra_duration  
            Send("{" extra_key " up}")  
        }  

        ; Random delay before the next cycle    
        cycle_delay := RandInt(min_cycle_delay, max_cycle_delay)  
        Sleep cycle_delay  
    }  
}  

; Generate random integer
RandInt(min, max)  
{  
    return Random(min, max)  
}  