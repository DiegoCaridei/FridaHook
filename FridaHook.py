# A script that creates a Frida skeleton script.
#@author Diego Caridei AKA Guybrush 
#@category Misc
#@keybinding 
#@menupath Tools.Misc.Mobile FridaHook
#@toolbar Tools.Misc.Mobile FridaHook


from ghidra.program.model.listing import Function
import os 

save = True

def extract_address(input_address):
    input_address = input_address.lstrip("0x")
    non_zero_flag = False    
    for char in input_address[-4:][::-1]:
        if char != '0':
            non_zero_flag = True
            break
    if len(input_address) >= 4 and non_zero_flag:
        extracted_substring = input_address[-6:]
        return "0x" + extracted_substring
    else:
        return "Invalid address format."

def writeFile(content):
    with open("script.js", 'w') as file:
        file.write(content)
    current_directory = os.getcwd()
    print("The location where the script.js file is stored is as follows: 
", current_directory)

current_program = getCurrentProgram()
current_location = 
currentProgram.getListing().getCodeUnitAt(currentAddress)

function = getFunctionContaining(current_location.getMinAddress())

if function:
    binary = currentProgram.getName()
    script = "var targetModule= '" + binary +"'"
    address = extract_address(function.getEntryPoint().toString())
    script += """
    var addr=ptr(%s);
    var moduleBase=Module.getBaseAddress(targetModule);
    var targetAddress=moduleBase.add(addr);
    Interceptor.attach(targetAddress,{
        onEnter:function(args){
            console.log("onEnter")
        },
        onLeave(retval){
            console.log("onLeave")
        }
    });
    """ %  address
    print(script)
    if save:
        writeFile(script)


else:
    print("No function at the current address.")


