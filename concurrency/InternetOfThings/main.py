from iot.devices import LightDevice, SmartSpeaker, SmartToilet
from iot.message import Message, MessageType
from iot.service import IOTService

def main() -> None: 
    #create a IOT service
    service = IOTService()
    
    # create and register a few devices
    light = LightDevice()
    speaker = SmartSpeaker()
    toilet = SmartToilet()
    light_id = service.register_device(light)
    speaker_id = service.register_device(speaker)
    toilet_id = service.register_device(toilet)
    
    #create a few programs
    wake_up_program = [
        Message(light_id, MessageType.SWITCH_ON),
        Message(speaker_id,MessageType.SWITCH_ON),
        Message(toilet_id,MessageType.PLAY_SONG,"Sam Smith - Lay Me Down")
    ]
    sleep_program = [
        Message(light_id, MessageType.SWITCH_OFF),
        Message(speaker_id,MessageType.SWITCH_OFF),
        Message(toilet_id,MessageType.FLUSH),
        Message(toilet_id,MessageType.CLEAN)
    ]
    
    service.run_program(wake_up_program)
    service.run_program(sleep_program)
    
if __name__ == "__main__":
    main()