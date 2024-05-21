from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def get_system_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    return current_volume

def set_system_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)

def mute_system_volume(mute):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(mute, None)

if __name__ == "__main__":
    
    current_volume = get_system_volume()
    print(f"Current Volume: {current_volume * 100}%")

    set = input("Enter the volume level (0-100): ")
    set_system_volume(int(set) / 100)
    print("Volume set to", set, "%")

    mute = input("Mute the system (True/False): ")
    if mute.lower() == "true":
        mute_system_volume(True)
        print("System muted")
    else:
        print("System unmuted")
