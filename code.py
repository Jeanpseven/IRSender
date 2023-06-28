import upnpclient
import pyIRsend

def discover_devices():
    devices = upnpclient.discover()
    return devices

def control_device(device, ir_code):
    ir_sender = pyIRsend.IRsend()
    ir_sender.send(device, ir_code)

def main():
    devices = discover_devices()

    print("Dispositivos encontrados:")
    for i, device in enumerate(devices):
        print(f"{i+1}. {device.friendly_name}")

    choice = input("Escolha o número do dispositivo: ")
    device_index = int(choice) - 1

    ir_code = input("Digite o código IR para enviar: ")

    if device_index >= 0 and device_index < len(devices):
        selected_device = devices[device_index]
        control_device(selected_device, ir_code)
        print("Comando IR enviado com sucesso!")
    else:
        print("Dispositivo selecionado inválido.")

if __name__ == "__main__":
    main()
