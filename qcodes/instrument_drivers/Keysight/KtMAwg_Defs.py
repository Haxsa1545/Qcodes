
# *************************************************************************** 
#*---------------------------- Attribute Defines ---------------------------* 
#***************************************************************************

IVI_ATTR_BASE =                 1000000



IVI_INHERENT_ATTR_BASE =        (IVI_ATTR_BASE +  50000)   #  base for inherent capability attributes 



IVI_CLASS_ATTR_BASE =           (IVI_ATTR_BASE + 250000)   #  base for IVI-defined class attributes 



IVI_LXISYNC_ATTR_BASE =         (IVI_ATTR_BASE + 950000)   #  base for IviLxiSync attributes 



IVI_SPECIFIC_ATTR_BASE =        (IVI_ATTR_BASE + 150000)   #  base for attributes of specific drivers 



# ===== IVI Inherent Instrument Attributes ==============================    

# - Driver Identification 

KTMAWG_ATTR_SPECIFIC_DRIVER_DESCRIPTION =              (IVI_INHERENT_ATTR_BASE + 514)  #  ViString, read-only 
KTMAWG_ATTR_SPECIFIC_DRIVER_PREFIX =                   (IVI_INHERENT_ATTR_BASE + 302)  #  ViString, read-only 
KTMAWG_ATTR_SPECIFIC_DRIVER_VENDOR =                   (IVI_INHERENT_ATTR_BASE + 513)  #  ViString, read-only 
KTMAWG_ATTR_SPECIFIC_DRIVER_REVISION =                 (IVI_INHERENT_ATTR_BASE + 551)  #  ViString, read-only 
KTMAWG_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = (IVI_INHERENT_ATTR_BASE + 515)  #  ViInt32, read-only 
KTMAWG_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = (IVI_INHERENT_ATTR_BASE + 516)  #  ViInt32, read-only 

# - User Options 

KTMAWG_ATTR_RANGE_CHECK =                             (IVI_INHERENT_ATTR_BASE + 2)  #  ViBoolean, read-write 
KTMAWG_ATTR_QUERY_INSTRUMENT_STATUS =                 (IVI_INHERENT_ATTR_BASE + 3)  #  ViBoolean, read-write 
KTMAWG_ATTR_CACHE =                                   (IVI_INHERENT_ATTR_BASE + 4)  #  ViBoolean, read-write 
KTMAWG_ATTR_SIMULATE =                                (IVI_INHERENT_ATTR_BASE + 5)  #  ViBoolean, read-write 
KTMAWG_ATTR_RECORD_COERCIONS =                        (IVI_INHERENT_ATTR_BASE + 6)  #  ViBoolean, read-write 
KTMAWG_ATTR_INTERCHANGE_CHECK =                       (IVI_INHERENT_ATTR_BASE + 21)  #  ViBoolean, read-write 

# - Advanced Session Information 

KTMAWG_ATTR_LOGICAL_NAME =                            (IVI_INHERENT_ATTR_BASE + 305)  #  ViString, read-only 
KTMAWG_ATTR_IO_RESOURCE_DESCRIPTOR =                  (IVI_INHERENT_ATTR_BASE + 304)  #  ViString, read-only 
KTMAWG_ATTR_DRIVER_SETUP =                            (IVI_INHERENT_ATTR_BASE + 7)  #  ViString, read-only 

# - Driver Capabilities 

KTMAWG_ATTR_GROUP_CAPABILITIES =                      (IVI_INHERENT_ATTR_BASE + 401)  #  ViString, read-only 
KTMAWG_ATTR_SUPPORTED_INSTRUMENT_MODELS =             (IVI_INHERENT_ATTR_BASE + 327)  #  ViString, read-only 

# - Instrument Identification 

KTMAWG_ATTR_INSTRUMENT_FIRMWARE_REVISION =            (IVI_INHERENT_ATTR_BASE + 510)  #  ViString, read-only 
KTMAWG_ATTR_INSTRUMENT_MANUFACTURER =                 (IVI_INHERENT_ATTR_BASE + 511)  #  ViString, read-only 
KTMAWG_ATTR_INSTRUMENT_MODEL =                        (IVI_INHERENT_ATTR_BASE + 512)  #  ViString, read-only 


# ===== Instrument-Specific Attributes =====================================

# - Instrument Specific 

KTMAWG_ATTR_GENERATION_SETTINGS_RESTRICTIONS =        (IVI_SPECIFIC_ATTR_BASE + 101)  #  ViBoolean, read-only 

# - System 

KTMAWG_ATTR_SERIAL_NUMBER =                           (IVI_SPECIFIC_ATTR_BASE + 3)  #  ViString, read-only 
KTMAWG_ATTR_SYSTEM_ABOUT =                            (IVI_SPECIFIC_ATTR_BASE + 4)  #  ViString, read-only 
KTMAWG_ATTR_SYSTEM_GC_TIMING_OPTIMIZATION_ENABLED =   (IVI_SPECIFIC_ATTR_BASE + 5)  #  ViBoolean, read-write 
KTMAWG_ATTR_SYSTEM_IDENTIFY_ENABLED =                 (IVI_SPECIFIC_ATTR_BASE + 6)  #  ViBoolean, read-write 
KTMAWG_ATTR_SYSTEM_INSTANCE_ID =                      (IVI_SPECIFIC_ATTR_BASE + 7)  #  ViInt32, read-only 
KTMAWG_ATTR_SYSTEM_OPTIONS =                          (IVI_SPECIFIC_ATTR_BASE + 8)  #  ViString, read-only 
KTMAWG_ATTR_SYSTEM_TIMEOUT =                          (IVI_SPECIFIC_ATTR_BASE + 9)  #  ViInt32, read-write 

# - Licensing 

KTMAWG_ATTR_LICENSING_HOST_IDENTIFIER =               (IVI_SPECIFIC_ATTR_BASE + 11)  #  ViString, read-only 
KTMAWG_ATTR_LICENSING_INSTALLED_LICENSES =            (IVI_SPECIFIC_ATTR_BASE + 12)  #  ViString, read-only 

# - Calibration 

KTMAWG_ATTR_CALIBRATION_ADJUSTMENT_INFORMATION =      (IVI_SPECIFIC_ATTR_BASE + 16)  #  ViString, read-only 
KTMAWG_ATTR_CALIBRATION_DUE_DATE =                    (IVI_SPECIFIC_ATTR_BASE + 17)  #  ViString, read-only 
KTMAWG_ATTR_CALIBRATION_INSTRUMENT_IDENTIFIER =       (IVI_SPECIFIC_ATTR_BASE + 18)  #  ViString, read-only 
KTMAWG_ATTR_CALIBRATION_STATUS =                      (IVI_SPECIFIC_ATTR_BASE + 19)  #  ViInt32, read-only 
KTMAWG_ATTR_CALIBRATION_VERIFICATION_INFORMATION =    (IVI_SPECIFIC_ATTR_BASE + 20)  #  ViString, read-only 

# - Module 

KTMAWG_ATTR_MODULE_COUNT =                            (IVI_SPECIFIC_ATTR_BASE + 23)  #  ViInt32, read-only 
KTMAWG_ATTR_MODULE_INSTRUMENT_CAPABILITY =            (IVI_SPECIFIC_ATTR_BASE + 24)  #  ViString, read-only 
KTMAWG_ATTR_MODULE_MAXIMUM_RECORDED_TEMPERATURE =     (IVI_SPECIFIC_ATTR_BASE + 25)  #  ViInt32, read-only 
KTMAWG_ATTR_MODULE_OPTIONS =                          (IVI_SPECIFIC_ATTR_BASE + 26)  #  ViString, read-only 
KTMAWG_ATTR_MODULE_SERIAL_NUMBER =                    (IVI_SPECIFIC_ATTR_BASE + 27)  #  ViString, read-only 
KTMAWG_ATTR_MODULE_SLOT =                             (IVI_SPECIFIC_ATTR_BASE + 28)  #  ViInt32, read-only 
KTMAWG_ATTR_MODULE_TEMPERATURE =                      (IVI_SPECIFIC_ATTR_BASE + 29)  #  ViReal64, read-only 

# - Calibration 

KTMAWG_ATTR_MODULE_CALIBRATION_ADJUSTMENT_INFORMATION =   (IVI_SPECIFIC_ATTR_BASE + 30)  #  ViString, read-only 
KTMAWG_ATTR_MODULE_CALIBRATION_DUE_DATE =                 (IVI_SPECIFIC_ATTR_BASE + 31)  #  ViString, read-only 
KTMAWG_ATTR_MODULE_CALIBRATION_STATUS =                   (IVI_SPECIFIC_ATTR_BASE + 32)  #  ViInt32, read-only 
KTMAWG_ATTR_MODULE_CALIBRATION_VERIFICATION_INFORMATION = (IVI_SPECIFIC_ATTR_BASE + 33)  #  ViString, read-only 

# - Nonvolatile 

KTMAWG_ATTR_NONVOLATILE_ASSET_NUMBER =                   (IVI_SPECIFIC_ATTR_BASE + 34)  #  ViString, read-write 
KTMAWG_ATTR_NONVOLATILE_CAL_DUE_REMINDER =               (IVI_SPECIFIC_ATTR_BASE + 35)  #  ViInt32, read-write 
KTMAWG_ATTR_NONVOLATILE_ENABLE_INSTRUMENT_CAL_WARNINGS = (IVI_SPECIFIC_ATTR_BASE + 36)  #  ViBoolean, read-write 
KTMAWG_ATTR_NONVOLATILE_ENABLE_MODULE_CAL_WARNINGS =     (IVI_SPECIFIC_ATTR_BASE + 37)  #  ViBoolean, read-write 
KTMAWG_ATTR_NONVOLATILE_ENABLE_PERIODIC_CAL =            (IVI_SPECIFIC_ATTR_BASE + 38)  #  ViBoolean, read-write 
KTMAWG_ATTR_NONVOLATILE_INSTRUMENT_CAL_INTERVAL =        (IVI_SPECIFIC_ATTR_BASE + 39)  #  ViInt32, read-write 
KTMAWG_ATTR_NONVOLATILE_MODULE_CAL_INTERVAL =            (IVI_SPECIFIC_ATTR_BASE + 40)  #  ViInt32, read-write 
KTMAWG_ATTR_NONVOLATILE_PASSPHRASE =                     (IVI_SPECIFIC_ATTR_BASE + 41)  #  ViString, read-write 
KTMAWG_ATTR_NONVOLATILE_SYSTEM_IDENTIFICATION =          (IVI_SPECIFIC_ATTR_BASE + 42)  #  ViString, read-write 

# - AssetChannel 

KTMAWG_ATTR_ASSETCHANNEL_COUNT =                      (IVI_SPECIFIC_ATTR_BASE + 60)  #  ViInt32, read-only 

# - PeerToPeerPort 

KTMAWG_ATTR_PEERTOPEERPORT_COUNT =                    (IVI_SPECIFIC_ATTR_BASE + 45)  #  ViInt32, read-only 
KTMAWG_ATTR_ACTIVE_PEERTOPEERPORT =                   (IVI_SPECIFIC_ATTR_BASE + 46)  #  ViString, read-write 

# - DeviceSync 

KTMAWG_ATTR_DEVICE_SYNC_CLOCK_RATE =                  (IVI_SPECIFIC_ATTR_BASE + 88)  #  ViInt32, read-write 
KTMAWG_ATTR_DEVICE_SYNC_CLOCK_SOURCE =                (IVI_SPECIFIC_ATTR_BASE + 89)  #  ViString, read-write 
KTMAWG_ATTR_DEVICE_SYNC_GROUP_MASK =                  (IVI_SPECIFIC_ATTR_BASE + 90)  #  ViInt32, read-write 
KTMAWG_ATTR_DEVICE_SYNC_GROUP_SIGNAL =                (IVI_SPECIFIC_ATTR_BASE + 91)  #  ViInt32, read-write 
KTMAWG_ATTR_DEVICE_SYNC_ROLE =                        (IVI_SPECIFIC_ATTR_BASE + 92)  #  ViInt32, read-write 
KTMAWG_ATTR_DEVICE_SYNC_SLAVE_SIGNAL =                (IVI_SPECIFIC_ATTR_BASE + 93)  #  ViInt32, read-write 
KTMAWG_ATTR_DEVICE_SYNC_STATE =                       (IVI_SPECIFIC_ATTR_BASE + 94)  #  ViInt32, read-only 
KTMAWG_ATTR_DEVICE_SYNC_IS_ALIGNMENT_VALID =          (IVI_SPECIFIC_ATTR_BASE + 97)  #  ViBoolean, read-only 
KTMAWG_ATTR_DEVICE_SYNC_SYNC_CHANNELS =               (IVI_SPECIFIC_ATTR_BASE + 100)  #  ViString, read-write 

# - Waveform 

KTMAWG_ATTR_ARB_NUMBER_WAVEFORMS =                    (IVI_SPECIFIC_ATTR_BASE + 98)  #  ViInt32, read-only 

# - Sequence 

KTMAWG_ATTR_ARB_NUMBER_SEQUENCES =                    (IVI_SPECIFIC_ATTR_BASE + 99)  #  ViInt32, read-only 

# - SequenceTriggers 

KTMAWG_ATTR_SEQUENCETRIGGER_MAX_COUNT =               (IVI_SPECIFIC_ATTR_BASE + 73)  #  ViInt32, read-only 
KTMAWG_ATTR_SEQUENCETRIGGER_COUNT =                   (IVI_SPECIFIC_ATTR_BASE + 74)  #  ViInt32, read-only 

# - Marker 

KTMAWG_ATTR_MARKER_COUNT =                            (IVI_SPECIFIC_ATTR_BASE + 75)  #  ViInt32, read-only 
KTMAWG_ATTR_MARKER_MAX_COUNT =                        (IVI_SPECIFIC_ATTR_BASE + 76)  #  ViInt32, read-only 

# - External 

KTMAWG_ATTR_EXTERNAL_COUNT =                          (IVI_SPECIFIC_ATTR_BASE + 79)  #  ViInt32, read-only 
KTMAWG_ATTR_EXTERNAL_INPUT_SLOPE =                    (IVI_SPECIFIC_ATTR_BASE + 83)  #  ViInt32, read-write 
KTMAWG_ATTR_EXTERNAL_OUTPUT_POLARITY =                (IVI_SPECIFIC_ATTR_BASE + 84)  #  ViInt32, read-write 
KTMAWG_ATTR_EXTERNAL_THRESHOLD =                      (IVI_SPECIFIC_ATTR_BASE + 85)  #  ViReal64, read-write 

# - TriggerBusLine 

KTMAWG_ATTR_TRIGGER_BUS_LINE_COUNT =                  (IVI_SPECIFIC_ATTR_BASE + 80)  #  ViInt32, read-only 
KTMAWG_ATTR_TRIGGER_BUS_LINE_INPUT_SLOPE =            (IVI_SPECIFIC_ATTR_BASE + 81)  #  ViInt32, read-write 
KTMAWG_ATTR_TRIGGER_BUS_LINE_OUTPUT_POLARITY =        (IVI_SPECIFIC_ATTR_BASE + 82)  #  ViInt32, read-write 
KTMAWG_ATTR_TRIGGER_BUS_LINE_CAPABILITY =             (IVI_SPECIFIC_ATTR_BASE + 86)  #  ViInt32, read-only 

# - ReferenceClock 

KTMAWG_ATTR_REF_CLOCK_IS_PHASE_LOCKED =               (IVI_SPECIFIC_ATTR_BASE + 96)  #  ViBoolean, read-only 

# - Arbitrary 

KTMAWG_ATTR_ARB_GAIN =                                (IVI_CLASS_ATTR_BASE + 202)  #  ViReal64, read-write 
KTMAWG_ATTR_ARB_OFFSET =                              (IVI_CLASS_ATTR_BASE + 203)  #  ViReal64, read-write 
KTMAWG_ATTR_ARB_SAMPLE_RATE =                         (IVI_CLASS_ATTR_BASE + 204)  #  ViReal64, read-write 

# - Waveform 

KTMAWG_ATTR_ARB_WAVEFORM_HANDLE =                     (IVI_CLASS_ATTR_BASE + 201)  #  ViInt32, read-write 
KTMAWG_ATTR_MAX_NUM_WAVEFORMS =                       (IVI_CLASS_ATTR_BASE + 205)  #  ViInt32, read-only 
KTMAWG_ATTR_WAVEFORM_QUANTUM =                        (IVI_CLASS_ATTR_BASE + 206)  #  ViInt32, read-only 
KTMAWG_ATTR_MAX_WAVEFORM_SIZE =                       (IVI_CLASS_ATTR_BASE + 208)  #  ViInt32, read-only 
KTMAWG_ATTR_MAX_WAVEFORM_SIZE64 =                     (IVI_CLASS_ATTR_BASE + 222)  #  ViInt64, read-only 
KTMAWG_ATTR_MIN_WAVEFORM_SIZE =                       (IVI_CLASS_ATTR_BASE + 207)  #  ViInt32, read-only 
KTMAWG_ATTR_MIN_WAVEFORM_SIZE64 =                     (IVI_CLASS_ATTR_BASE + 221)  #  ViInt64, read-only 
KTMAWG_ATTR_BINARY_ALIGNMENT =                        (IVI_CLASS_ATTR_BASE + 241)  #  ViInt32, read-only 
KTMAWG_ATTR_SAMPLE_BIT_RESOLUTION =                   (IVI_CLASS_ATTR_BASE + 242)  #  ViInt32, read-only 
KTMAWG_ATTR_OUTPUT_DATA_MASK =                        (IVI_CLASS_ATTR_BASE + 261)  #  ViInt32, read-only 

# - Sequence 

KTMAWG_ATTR_ARB_SEQUENCE_HANDLE =                     (IVI_CLASS_ATTR_BASE + 211)  #  ViInt32, read-write 
KTMAWG_ATTR_MAX_SEQUENCE_LENGTH =                     (IVI_CLASS_ATTR_BASE + 214)  #  ViInt32, read-only 
KTMAWG_ATTR_MIN_SEQUENCE_LENGTH =                     (IVI_CLASS_ATTR_BASE + 213)  #  ViInt32, read-only 
KTMAWG_ATTR_MAX_LOOP_COUNT =                          (IVI_CLASS_ATTR_BASE + 215)  #  ViInt32, read-only 
KTMAWG_ATTR_MAX_NUM_SEQUENCES =                       (IVI_CLASS_ATTR_BASE + 212)  #  ViInt32, read-only 
KTMAWG_ATTR_MAX_SEQUENCE_DEPTH =                      (IVI_CLASS_ATTR_BASE + 281)  #  ViInt32, read-only 

# - Output 

KTMAWG_ATTR_CHANNEL_COUNT =                           (IVI_INHERENT_ATTR_BASE + 203)  #  ViInt32, read-only 
KTMAWG_ATTR_OUTPUT_ENABLED =                          (IVI_CLASS_ATTR_BASE + 3)  #  ViBoolean, read-write 
KTMAWG_ATTR_OUTPUT_IMPEDANCE =                        (IVI_CLASS_ATTR_BASE + 4)  #  ViReal64, read-write 
KTMAWG_ATTR_OPERATION_MODE =                          (IVI_CLASS_ATTR_BASE + 5)  #  ViInt32, read-write 
KTMAWG_ATTR_OUTPUT_MODE =                             (IVI_CLASS_ATTR_BASE + 1)  #  ViInt32, read-write 
KTMAWG_ATTR_REF_CLOCK_SOURCE =                        (IVI_CLASS_ATTR_BASE + 2)  #  ViInt32, read-write 
KTMAWG_ATTR_TERMINAL_CONFIGURATION =                  (IVI_CLASS_ATTR_BASE + 31)  #  ViInt32, read-write 

# - Trigger 

KTMAWG_ATTR_BURST_COUNT =                             (IVI_CLASS_ATTR_BASE + 350)  #  ViInt32, read-write 
KTMAWG_ATTR_TRIGGER_SOURCE =                          (IVI_CLASS_ATTR_BASE + 302)  #  ViInt32, read-write 

# - Start Trigger 

KTMAWG_ATTR_START_TRIGGER_DELAY =                     (IVI_CLASS_ATTR_BASE + 320)  #  ViReal64, read-write 
KTMAWG_ATTR_START_TRIGGER_SLOPE =                     (IVI_CLASS_ATTR_BASE + 321)  #  ViInt32, read-write 
KTMAWG_ATTR_START_TRIGGER_SOURCE =                    (IVI_CLASS_ATTR_BASE + 322)  #  ViString, read-write 
KTMAWG_ATTR_START_TRIGGER_THRESHOLD =                 (IVI_CLASS_ATTR_BASE + 323)  #  ViReal64, read-write 


# *************************************************************************** 
# *------------------------ Attribute Value Defines -------------------------* 
# ***************************************************************************

# - Defined values for 

KTMAWG_VAL_STATUS_BYTE_FLAGS_USER0 =                  1
KTMAWG_VAL_STATUS_BYTE_FLAGS_USER1 =                  2
KTMAWG_VAL_STATUS_BYTE_FLAGS_USER2 =                  4
KTMAWG_VAL_STATUS_BYTE_FLAGS_USER3 =                  8
KTMAWG_VAL_STATUS_BYTE_FLAGS_MESSAGE_AVAILABLE =      16
KTMAWG_VAL_STATUS_BYTE_FLAGS_EVENT_STATUS_REGISTER =  32
KTMAWG_VAL_STATUS_BYTE_FLAGS_REQUESTING_SERVICE =     64
KTMAWG_VAL_STATUS_BYTE_FLAGS_USER7 =                  128

# - Defined values for 

KTMAWG_VAL_UPDATE_STATUS_IN_PROGRESS =                0
KTMAWG_VAL_UPDATE_STATUS_SUCCESS =                    1
KTMAWG_VAL_UPDATE_STATUS_RESTART_REQUIRED =           2
KTMAWG_VAL_UPDATE_STATUS_POWER_CYCLE_REQUIRED =       3
KTMAWG_VAL_UPDATE_STATUS_FAILED =                     4

# - Defined values for 
#   attribute KTMAWG_ATTR_CALIBRATION_STATUS
#   attribute KTMAWG_ATTR_MODULE_CALIBRATION_STATUS 

KTMAWG_VAL_CALIBRATION_STATUS_DUE =                        1
KTMAWG_VAL_CALIBRATION_STATUS_EXPIRED =                    2
KTMAWG_VAL_CALIBRATION_STATUS_INSTRUMENT_CALIBRATED =      0
KTMAWG_VAL_CALIBRATION_STATUS_MODULES_CALIBRATED =         5
KTMAWG_VAL_CALIBRATION_STATUS_NOT_CALIBRATED =             3
KTMAWG_VAL_CALIBRATION_STATUS_NOT_SUBJECT_TO_CALIBRATION = 4

# - Defined values for 
#    parameter Mask in function KtMAwg_StatusClearEvent
#    parameter Mask in function KtMAwg_StatusGetEventState
#    parameter Mask in function KtMAwg_StatusSetEvent 

KTMAWG_VAL_STATUS_EVENT_ALL =                         0
KTMAWG_VAL_STATUS_EVENT_ERROR_IN_QUEUE =              1
KTMAWG_VAL_STATUS_EVENT_THERMAL_SHUTDOWN =            14
KTMAWG_VAL_STATUS_EVENT_THERMAL_WARNING =             15
KTMAWG_VAL_STATUS_EVENT_USER_DEFINED =                2

# - Defined values for 

KTMAWG_VAL_MODULE_EVENT_ALL =                         0
KTMAWG_VAL_MODULE_EVENT_TIMER1 =                      201
KTMAWG_VAL_MODULE_EVENT_TIMER2 =                      202
KTMAWG_VAL_MODULE_EVENT_TIMER3 =                      203
KTMAWG_VAL_MODULE_EVENT_TIMER4 =                      204
KTMAWG_VAL_MODULE_EVENT_TRIGGER1 =                    1
KTMAWG_VAL_MODULE_EVENT_TRIGGER10 =                   10
KTMAWG_VAL_MODULE_EVENT_TRIGGER2 =                    2
KTMAWG_VAL_MODULE_EVENT_TRIGGER3 =                    3
KTMAWG_VAL_MODULE_EVENT_TRIGGER4 =                    4
KTMAWG_VAL_MODULE_EVENT_TRIGGER5 =                    5
KTMAWG_VAL_MODULE_EVENT_TRIGGER6 =                    6
KTMAWG_VAL_MODULE_EVENT_TRIGGER7 =                    7
KTMAWG_VAL_MODULE_EVENT_TRIGGER8 =                    8
KTMAWG_VAL_MODULE_EVENT_TRIGGER9 =                    9
KTMAWG_VAL_MODULE_EVENT_USER1 =                       101
KTMAWG_VAL_MODULE_EVENT_USER2 =                       102
KTMAWG_VAL_MODULE_EVENT_USER3 =                       103
KTMAWG_VAL_MODULE_EVENT_USER4 =                       104

# - Defined values for 

KTMAWG_VAL_SPI_MODE_LSB_FIRST_BYTE =                  0
KTMAWG_VAL_SPI_MODE_LSB_FIRST_WORD =                  1
KTMAWG_VAL_SPI_MODE_MSB_FIRST_BYTE =                  2
KTMAWG_VAL_SPI_MODE_MSB_FIRST_WORD =                  3

# - Defined values for 

KTMAWG_VAL_TRIGGER_DIRECTION_INPUT =                  0
KTMAWG_VAL_TRIGGER_DIRECTION_OUTPUT =                 1

# - Defined values for 

KTMAWG_VAL_TRIGGER_MODE_LEVEL =                       1
KTMAWG_VAL_TRIGGER_MODE_PULSE =                       0

# - Defined values for 

KTMAWG_VAL_TRIGGER_POLARITY_NEGATIVE =                1
KTMAWG_VAL_TRIGGER_POLARITY_POSITIVE =                0

# - Defined values for 

KTMAWG_VAL_TRIGGER_PXI_TRIGGER0 =                     0
KTMAWG_VAL_TRIGGER_PXI_TRIGGER1 =                     1
KTMAWG_VAL_TRIGGER_PXI_TRIGGER2 =                     2
KTMAWG_VAL_TRIGGER_PXI_TRIGGER3 =                     3
KTMAWG_VAL_TRIGGER_PXI_TRIGGER4 =                     4
KTMAWG_VAL_TRIGGER_PXI_TRIGGER5 =                     5
KTMAWG_VAL_TRIGGER_PXI_TRIGGER6 =                     6
KTMAWG_VAL_TRIGGER_PXI_TRIGGER7 =                     7

# - Defined values for 

KTMAWG_VAL_TRIGGER_RESOURCE_NONE =                    -1
KTMAWG_VAL_TRIGGER_RESOURCE_TRIGGER1 =                0
KTMAWG_VAL_TRIGGER_RESOURCE_TRIGGER2 =                1
KTMAWG_VAL_TRIGGER_RESOURCE_TRIGGER3 =                2
KTMAWG_VAL_TRIGGER_RESOURCE_TRIGGER4 =                3
KTMAWG_VAL_TRIGGER_RESOURCE_TRIGGER5 =                4
KTMAWG_VAL_TRIGGER_RESOURCE_TRIGGER6 =                5
KTMAWG_VAL_TRIGGER_RESOURCE_TRIGGER7 =                6
KTMAWG_VAL_TRIGGER_RESOURCE_TRIGGER8 =                7
KTMAWG_VAL_TRIGGER_RESOURCE_TRIGGER9 =                8
KTMAWG_VAL_TRIGGER_RESOURCE_TRIGGER10 =               9

# - Defined values for 

KTMAWG_VAL_TRIGGER_TERMINATION_HIGH_IMPEDANCE =       0
KTMAWG_VAL_TRIGGER_TERMINATION_LOW_IMPEDANCE =        1

# - Defined values for 

KTMAWG_VAL_LTC3880_PHASE_BOTH_PHASES =                255
KTMAWG_VAL_LTC3880_PHASE_PHASE0 =                     0
KTMAWG_VAL_LTC3880_PHASE_PHASE1 =                     1

# - Defined values for 

KTMAWG_VAL_SELF_TEST_ADC_MEASUREMENT_MODE_COMMON_REFERENCE = 1
KTMAWG_VAL_SELF_TEST_ADC_MEASUREMENT_MODE_DIFFERENTIAL =     0

# - Defined values for 

KTMAWG_VAL_SELF_TEST_ADC_MEASUREMENT_RANGE_VOLTAGE_0P64 =   5
KTMAWG_VAL_SELF_TEST_ADC_MEASUREMENT_RANGE_VOLTAGE1_0P24 =  1
KTMAWG_VAL_SELF_TEST_ADC_MEASUREMENT_RANGE_VOLTAGE_1P28 =   4
KTMAWG_VAL_SELF_TEST_ADC_MEASUREMENT_RANGE_VOLTAGE2_0P48 =  7
KTMAWG_VAL_SELF_TEST_ADC_MEASUREMENT_RANGE_VOLTAGE2_4P576 = 0
KTMAWG_VAL_SELF_TEST_ADC_MEASUREMENT_RANGE_VOLTAGE_2P56 =   3
KTMAWG_VAL_SELF_TEST_ADC_MEASUREMENT_RANGE_VOLTAGE_5P12 =   2

# - Defined values for 
#    parameter State in function KtMAwg_GetGenerationStateByChannel 

KTMAWG_VAL_GENERATION_STATE_CONFIGURATION =           0
KTMAWG_VAL_GENERATION_STATE_OUTPUT_GENERATION =       1

# - Defined values for 

KTMAWG_VAL_MEMORY_QUERY_MODE_TOTAL_SIZE =             0
KTMAWG_VAL_MEMORY_QUERY_MODE_FREE_SIZE =              1
KTMAWG_VAL_MEMORY_QUERY_MODE_ALLOCATED_SIZE =         2

# - Defined values for 
#    parameter Mode in function KtMAwg_CorrectionsGetFilterMode
#    parameter Mode in function KtMAwg_CorrectionsSetFilterMode 

KTMAWG_VAL_CORRECTION_FILTER_MODE_UNCALIBRATED =      1
KTMAWG_VAL_CORRECTION_FILTER_MODE_BYPASS =            2
KTMAWG_VAL_CORRECTION_FILTER_MODE_CALIBRATED =        0

# - Defined values for 

KTMAWG_VAL_ATTRIBUTES_ARBITRARY_SAMPLE_RATE =         0
KTMAWG_VAL_ATTRIBUTES_OUTPUT_DELAY =                  4
KTMAWG_VAL_ATTRIBUTES_MARKER_DELAY =                  20
KTMAWG_VAL_ATTRIBUTES_ARBITRARY_GAIN =                10
KTMAWG_VAL_ATTRIBUTES_ARBITRARY_ANALOG_GAIN =         13
KTMAWG_VAL_ATTRIBUTES_ARBITRARY_DIGITAL_GAIN =        14
KTMAWG_VAL_ATTRIBUTES_ARBITRARY_OFFSET =              11
KTMAWG_VAL_ATTRIBUTES_ARBITRARY_COMMON_MODE_OFFSET =  12
KTMAWG_VAL_ATTRIBUTES_ARBITRARY_LOAD_IMPEDANCE =      8
KTMAWG_VAL_ATTRIBUTES_START_TRIGGER_DELAY =           16
KTMAWG_VAL_ATTRIBUTES_START_TRIGGER_SOURCE =          15
KTMAWG_VAL_ATTRIBUTES_MARKER_DESTINATION =            19
KTMAWG_VAL_ATTRIBUTES_MARKER_BIT_POSITION =           21
KTMAWG_VAL_ATTRIBUTES_SEQUENCE_TRIGGER_SOURCE =       17
KTMAWG_VAL_ATTRIBUTES_SEQUENCE_TRIGGER_DELAY =        18
KTMAWG_VAL_ATTRIBUTES_OUTPUT_OPERATION_MODE =         5
KTMAWG_VAL_ATTRIBUTES_ARBITRARY_GAIN_CONTROL =        9
KTMAWG_VAL_ATTRIBUTES_ARBITRARY_CHANNEL_MODE =        2
KTMAWG_VAL_ATTRIBUTES_ARBITRARY_HANDLE =              1
KTMAWG_VAL_ATTRIBUTES_OUTPUT_ENABLED =                3
KTMAWG_VAL_ATTRIBUTES_OUTPUT_TERMINAL_CONFIGURATION = 7
KTMAWG_VAL_ATTRIBUTES_CORRECTION_FILTER_MODE =        22
KTMAWG_VAL_ATTRIBUTES_BURST_COUNT =                   6
KTMAWG_VAL_ATTRIBUTES_ARBITRARY_WAVEFORM_MODE =       30

# - Defined values for 
#    parameter Control in function KtMAwg_ArbitrarySetGainControl
#    parameter Control in function KtMAwg_ArbitraryGetGainControl 

KTMAWG_VAL_GAIN_CONTROL_COMPONENT =                   1
KTMAWG_VAL_GAIN_CONTROL_COMPOSITE =                   0

# - Defined values for 
#    parameter Events in function KtMAwg_QueryGenerationEvents 

KTMAWG_VAL_GENERATION_EVENTS_NONE =                        0
KTMAWG_VAL_GENERATION_EVENTS_DIGITAL_GAIN_BLOCK_OVERFLOW = 1
KTMAWG_VAL_GENERATION_EVENTS_FIFO_UNDERRUN =               2
KTMAWG_VAL_GENERATION_EVENTS_RESAMPLER_OVERFLOW =          4
KTMAWG_VAL_GENERATION_EVENTS_CORRECTIONS_OVERFLOW =        8
KTMAWG_VAL_GENERATION_EVENTS_MARKER_QUEUE_OVERRUN =        16
KTMAWG_VAL_GENERATION_EVENTS_MARKER_IGNORED =              32
KTMAWG_VAL_GENERATION_EVENTS_STREAMING_DATA_UNDERRUN =     128

# - Defined values for 
#    attribute KTMAWG_ATTR_OUTPUT_MODE
#    parameter OutputMode in function KtMAwg_ConfigureOutputMode 

KTMAWG_VAL_OUTPUT_FUNC =                              0
KTMAWG_VAL_OUTPUT_ARB =                               1
KTMAWG_VAL_OUTPUT_SEQ =                               2

# - Defined values for 
#    attribute KTMAWG_ATTR_OPERATION_MODE
#    parameter OperationMode in function KtMAwg_ConfigureOperationMode 

KTMAWG_VAL_OPERATE_CONTINUOUS =                       0
KTMAWG_VAL_OPERATE_BURST =                            1

# - Defined values for 
#    attribute KTMAWG_ATTR_REF_CLOCK_SOURCE
#    parameter Source in function KtMAwg_ConfigureRefClockSource 

KTMAWG_VAL_REF_CLOCK_INTERNAL =                       0
KTMAWG_VAL_REF_CLOCK_EXTERNAL =                       1
KTMAWG_VAL_REF_CLOCK_RTSI_CLOCK =                     101

# - Defined values for 
#    attribute KTMAWG_ATTR_TRIGGER_SOURCE
#    parameter Source in function KtMAwg_ConfigureTriggerSource 

KTMAWG_VAL_EXTERNAL =                                 1
KTMAWG_VAL_SOFTWARE_TRIG =                            2
KTMAWG_VAL_INTERNAL_TRIGGER =                         3
KTMAWG_VAL_TTL0 =                                     111
KTMAWG_VAL_TTL1 =                                     112
KTMAWG_VAL_TTL2 =                                     113
KTMAWG_VAL_TTL3 =                                     114
KTMAWG_VAL_TTL4 =                                     115
KTMAWG_VAL_TTL5 =                                     116
KTMAWG_VAL_TTL6 =                                     117
KTMAWG_VAL_TTL7 =                                     118
KTMAWG_VAL_ECL0 =                                     119
KTMAWG_VAL_ECL1 =                                     120
KTMAWG_VAL_PXI_STAR =                                 131
KTMAWG_VAL_RTSI_0 =                                   141
KTMAWG_VAL_RTSI_1 =                                   142
KTMAWG_VAL_RTSI_2 =                                   143
KTMAWG_VAL_RTSI_3 =                                   144
KTMAWG_VAL_RTSI_4 =                                   145
KTMAWG_VAL_RTSI_5 =                                   146
KTMAWG_VAL_RTSI_6 =                                   147
KTMAWG_VAL_SOFTWARE0 =                                1001
KTMAWG_VAL_SOFTWARE1 =                                1002
KTMAWG_VAL_SOFTWARE2 =                                1003
KTMAWG_VAL_SOFTWARE3 =                                1004
KTMAWG_VAL_SOFTWARE4 =                                1005
KTMAWG_VAL_SOFTWARE5 =                                1006
KTMAWG_VAL_SOFTWARE6 =                                1007
KTMAWG_VAL_SOFTWARE7 =                                1008
KTMAWG_VAL_SOFTWARE9 =                                1010
KTMAWG_VAL_SOFTWARE10 =                               1011
KTMAWG_VAL_SOFTWARE11 =                               1012
KTMAWG_VAL_SOFTWARE12 =                               1013
KTMAWG_VAL_SOFTWARE13 =                               1014
KTMAWG_VAL_SOFTWARE14 =                               1015
KTMAWG_VAL_SOFTWARE15 =                               1016
KTMAWG_VAL_SOFTWARE8 =                                1009
KTMAWG_VAL_PXI_TRIG0 =                                1017
KTMAWG_VAL_PXI_TRIG1 =                                1018
KTMAWG_VAL_PXI_TRIG2 =                                1019
KTMAWG_VAL_PXI_TRIG3 =                                1020
KTMAWG_VAL_PXI_TRIG4 =                                1021
KTMAWG_VAL_PXI_TRIG5 =                                1022
KTMAWG_VAL_PXI_TRIG6 =                                1023
KTMAWG_VAL_PXI_TRIG7 =                                1024
KTMAWG_VAL_EXTERNAL1 =                                1025
KTMAWG_VAL_EXTERNAL2 =                                1026
KTMAWG_VAL_PXIE_DSTARB =                              1027
KTMAWG_VAL_DIO_0 =                                    1028
KTMAWG_VAL_DIO_1 =                                    1029
KTMAWG_VAL_DIO_2 =                                    1030
KTMAWG_VAL_DIO_3 =                                    1031
KTMAWG_VAL_DIO_4 =                                    1032
KTMAWG_VAL_DIO_5 =                                    1033
KTMAWG_VAL_DIO_7 =                                    1035
KTMAWG_VAL_DIO_6 =                                    1034
KTMAWG_VAL_TRIG_IMMEDIATE =                           1036
KTMAWG_VAL_DISABLED =                                 1037

# - Defined values for 

KTMAWG_VAL_WFM_SINE =                                 1
KTMAWG_VAL_WFM_SQUARE =                               2
KTMAWG_VAL_WFM_TRIANGLE =                             3
KTMAWG_VAL_WFM_RAMP_UP =                              4
KTMAWG_VAL_WFM_RAMP_DOWN =                            5
KTMAWG_VAL_WFM_DC =                                   6

# - Defined values for 

KTMAWG_VAL_AM_INTERNAL_SINE =                         1
KTMAWG_VAL_AM_INTERNAL_SQUARE =                       2
KTMAWG_VAL_AM_INTERNAL_TRIANGLE =                     3
KTMAWG_VAL_AM_INTERNAL_RAMP_UP =                      4
KTMAWG_VAL_AM_INTERNAL_RAMP_DOWN =                    5

# - Defined values for 

KTMAWG_VAL_AM_INTERNAL =                              0
KTMAWG_VAL_AM_EXTERNAL =                              1

# - Defined values for 

KTMAWG_VAL_FM_INTERNAL_SINE =                         1
KTMAWG_VAL_FM_INTERNAL_SQUARE =                       2
KTMAWG_VAL_FM_INTERNAL_TRIANGLE =                     3
KTMAWG_VAL_FM_INTERNAL_RAMP_UP =                      4
KTMAWG_VAL_FM_INTERNAL_RAMP_DOWN =                    5

# - Defined values for 

KTMAWG_VAL_FM_INTERNAL =                              0
KTMAWG_VAL_FM_EXTERNAL =                              1

# - Defined values for 
#    attribute KTMAWG_ATTR_START_TRIGGER_SLOPE
#    parameter Slope in function KtMAwg_ConfigureStartTrigger 

KTMAWG_VAL_TRIGGER_POSITIVE =                         0
KTMAWG_VAL_TRIGGER_NEGATIVE =                         1
KTMAWG_VAL_TRIGGER_EITHER =                           2

# - Defined values for 
#    attribute KTMAWG_ATTR_TERMINAL_CONFIGURATION
#    parameter Configuration in function KtMAwg_OutputSetTerminalConfiguration 

KTMAWG_VAL_TERMINAL_CONFIGURATION_SINGLE_ENDED =      0
KTMAWG_VAL_TERMINAL_CONFIGURATION_DIFFERENTIAL =      1

# - Defined values for 

KTMAWG_VAL_SAMPLE_CLOCK_SOURCE_INTERNAL =             0
KTMAWG_VAL_SAMPLE_CLOCK_SOURCE_EXTERNAL =             1

# - Defined values for 

KTMAWG_VAL_MARKER_POLARITY_ACTIVE_HIGH =              0
KTMAWG_VAL_MARKER_POLARITY_ACTIVE_LOW =               1

# - Defined values for 
#    attribute KTMAWG_ATTR_BINARY_ALIGNMENT 

KTMAWG_VAL_BINARY_ALIGNMENT_LEFT =                    0
KTMAWG_VAL_BINARY_ALIGNMENT_RIGHT =                   1

# - Defined values for 
#    parameter Mode in function KtMAwg_GetChannelMode
#    parameter Mode in function KtMAwg_SetChannelMode 

KTMAWG_VAL_CHANNEL_MODE_WAVEFORM =                    0
KTMAWG_VAL_CHANNEL_MODE_MARKER =                      1

# - Defined values for 

KTMAWG_VAL_EXTERNAL_IMPEDANCE_OHM_1K =                0
KTMAWG_VAL_EXTERNAL_IMPEDANCE_OHM50 =                 1

# - Defined values for 

KTMAWG_VAL_EXTERNAL_ATTRIBUTES_THRESHOLD =            0

# - Defined values for 
#    attribute KTMAWG_ATTR_EXTERNAL_INPUT_SLOPE
#    attribute KTMAWG_ATTR_TRIGGER_BUS_LINE_INPUT_SLOPE 

KTMAWG_VAL_INPUT_SLOPE_POSITIVE =                     0
KTMAWG_VAL_INPUT_SLOPE_NEGATIVE =                     1

# - Defined values for 
#    attribute KTMAWG_ATTR_EXTERNAL_OUTPUT_POLARITY
#    attribute KTMAWG_ATTR_TRIGGER_BUS_LINE_OUTPUT_POLARITY
#    parameter Val in function KtMAwg_GetChannelMarkerPolarity
#   parameter Polarity in function KtMAwg_SetChannelMarkerPolarity 

KTMAWG_VAL_OUTPUT_POLARITY_POSITIVE =                 0
KTMAWG_VAL_OUTPUT_POLARITY_NEGATIVE =                 1

# - Defined values for 
#    parameter Option in function KtMAwg_MemoryTest 

KTMAWG_VAL_MEMORY_TEST_STANDARD =                     1
KTMAWG_VAL_MEMORY_TEST_COMPREHENSIVE =                0

# - Defined values for 
#    attribute KTMAWG_ATTR_TRIGGER_BUS_LINE_CAPABILITY 

KTMAWG_VAL_TRIGGER_BUS_LINE_CAPABILITY_INPUT =        1
KTMAWG_VAL_TRIGGER_BUS_LINE_CAPABILITY_OUTPUT =       2
KTMAWG_VAL_TRIGGER_BUS_LINE_CAPABILITY_BOTH =         3

# - Defined values for 
#    attribute KTMAWG_ATTR_DEVICE_SYNC_GROUP_SIGNAL
#    attribute KTMAWG_ATTR_DEVICE_SYNC_SLAVE_SIGNAL
#    parameter GroupSignal in function KtMAwg_DeviceSyncConfigureMaster
#    parameter SlaveSignals in function KtMAwg_DeviceSyncConfigureMaster
#    parameter GroupSignal in function KtMAwg_DeviceSyncConfigureSlave
#    parameter SlaveSignal in function KtMAwg_DeviceSyncConfigureSlave
#    parameter Val in function KtMAwg_DeviceSyncGetGroupMask
#    parameter SlaveSignals in function KtMAwg_DeviceSyncSetGroupMask 

KTMAWG_VAL_DEVICE_SYNC_RESOURCESFP_SYNC =             32768
KTMAWG_VAL_DEVICE_SYNC_RESOURCES_NONE =               0
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXI_LBL6 =            2048
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXI_LBR6 =            1024
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXI_STAR =            512
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXI_TRIG0 =           1
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXI_TRIG1 =           2
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXI_TRIG2 =           4
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXI_TRIG3 =           8
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXI_TRIG4 =           16
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXI_TRIG5 =           32
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXI_TRIG6 =           64
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXI_TRIG7 =           128
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXIE_DSTARA =         4096
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXIE_DSTARB =         8192
KTMAWG_VAL_DEVICE_SYNC_RESOURCESPXIE_DSTARC =         16384

# - Defined values for 
#    attribute KTMAWG_ATTR_DEVICE_SYNC_ROLE
#    parameter Role in function KtMAwg_DeviceSyncConfigureMaster 

KTMAWG_VAL_DEVICE_SYNC_ROLE_GROUP_MASTER =            3
KTMAWG_VAL_DEVICE_SYNC_ROLE_LOCAL_MASTER =            5
KTMAWG_VAL_DEVICE_SYNC_ROLE_OFF =                     0
KTMAWG_VAL_DEVICE_SYNC_ROLE_SLAVE =                   2
KTMAWG_VAL_DEVICE_SYNC_ROLE_SANDBOX =                 1
KTMAWG_VAL_DEVICE_SYNC_ROLE_SYSTEM_MASTER =           4

# - Defined values for 
#    attribute KTMAWG_ATTR_DEVICE_SYNC_STATE 

KTMAWG_VAL_DEVICE_SYNC_STATE_ARM =                    1
KTMAWG_VAL_DEVICE_SYNC_STATE_IDLE =                   0
KTMAWG_VAL_DEVICE_SYNC_STATE_RUN =                    3
KTMAWG_VAL_DEVICE_SYNC_STATE_TRIGGER =                2
KTMAWG_VAL_DEVICE_SYNC_STATE_UNKNOWN =                4

# - Defined values for 
#    parameter State in function KtMAwg_GetOutputGenerationState 

KTMAWG_VAL_OUTPUT_GENERATION_STATE_IDLE =             0
KTMAWG_VAL_OUTPUT_GENERATION_STATE_ARM =              1
KTMAWG_VAL_OUTPUT_GENERATION_STATE_TRIGGER =          2
KTMAWG_VAL_OUTPUT_GENERATION_STATE_RUN =              3
KTMAWG_VAL_OUTPUT_GENERATION_STATE_UNKNOWN =          4

# - Defined values for 
#    parameter Val in function KtMAwg_GetWaveformMode
#    parameter Mode in function KtMAwg_SetWaveformMode 

KTMAWG_VAL_WAVEFORM_MODE_CATALOGED =                  0
KTMAWG_VAL_WAVEFORM_MODE_STREAMING =                  1


# *************************************************************************** 
# *----------------- Instrument Error And Completion Codes ------------------* 
# ***************************************************************************

IVIC_WARN_BASE =                           (0x3FFA0000)
IVIC_CROSS_CLASS_WARN_BASE =               (IVIC_WARN_BASE + 0x1000)
IVIC_CLASS_WARN_BASE =                     (IVIC_WARN_BASE + 0x2000)
IVIC_SPECIFIC_WARN_BASE =                  (IVIC_WARN_BASE + 0x4000)

IVIC_ERROR_BASE =                          (0xBFFA0000)
IVIC_CROSS_CLASS_ERROR_BASE =              (IVIC_ERROR_BASE + 0x1000)
IVIC_CLASS_ERROR_BASE =                    (IVIC_ERROR_BASE + 0x2000)
IVIC_SPECIFIC_ERROR_BASE =                 (IVIC_ERROR_BASE + 0x4000)
IVIC_LXISYNC_ERROR_BASE =                  (IVIC_ERROR_BASE + 0x2000)




KTMAWG_ERROR_CANNOT_RECOVER =                         (IVIC_ERROR_BASE + 0x0000)
KTMAWG_ERROR_INSTRUMENT_STATUS =                      (IVIC_ERROR_BASE + 0x0001)
KTMAWG_ERROR_CANNOT_OPEN_FILE =                       (IVIC_ERROR_BASE + 0x0002)
KTMAWG_ERROR_READING_FILE =                           (IVIC_ERROR_BASE + 0x0003)
KTMAWG_ERROR_WRITING_FILE =                           (IVIC_ERROR_BASE + 0x0004)
KTMAWG_ERROR_INVALID_PATHNAME =                       (IVIC_ERROR_BASE + 0x000B)
KTMAWG_ERROR_INVALID_ATTRIBUTE =                      (IVIC_ERROR_BASE + 0x000C)
KTMAWG_ERROR_IVI_ATTR_NOT_WRITABLE =                  (IVIC_ERROR_BASE + 0x000D)
KTMAWG_ERROR_IVI_ATTR_NOT_READABLE =                  (IVIC_ERROR_BASE + 0x000E)
KTMAWG_ERROR_INVALID_VALUE =                          (IVIC_ERROR_BASE + 0x0010)
KTMAWG_ERROR_FUNCTION_NOT_SUPPORTED =                 (IVIC_ERROR_BASE + 0x0011)
KTMAWG_ERROR_ATTRIBUTE_NOT_SUPPORTED =                (IVIC_ERROR_BASE + 0x0012)
KTMAWG_ERROR_VALUE_NOT_SUPPORTED =                    (IVIC_ERROR_BASE + 0x0013)
KTMAWG_ERROR_TYPES_DO_NOT_MATCH =                     (IVIC_ERROR_BASE + 0x0015)
KTMAWG_ERROR_NOT_INITIALIZED =                        (IVIC_ERROR_BASE + 0x001D)
KTMAWG_ERROR_UNKNOWN_CHANNEL_NAME =                   (IVIC_ERROR_BASE + 0x0020)
KTMAWG_ERROR_TOO_MANY_OPEN_FILES =                    (IVIC_ERROR_BASE + 0x0023)
KTMAWG_ERROR_CHANNEL_NAME_REQUIRED =                  (IVIC_ERROR_BASE + 0x0044)
KTMAWG_ERROR_MISSING_OPTION_NAME =                    (IVIC_ERROR_BASE + 0x0049)
KTMAWG_ERROR_MISSING_OPTION_VALUE =                   (IVIC_ERROR_BASE + 0x004A)
KTMAWG_ERROR_BAD_OPTION_NAME =                        (IVIC_ERROR_BASE + 0x004B)
KTMAWG_ERROR_BAD_OPTION_VALUE =                       (IVIC_ERROR_BASE + 0x004C)
KTMAWG_ERROR_OUT_OF_MEMORY =                          (IVIC_ERROR_BASE + 0x0056)
KTMAWG_ERROR_OPERATION_PENDING =                      (IVIC_ERROR_BASE + 0x0057)
KTMAWG_ERROR_NULL_POINTER =                           (IVIC_ERROR_BASE + 0x0058)
KTMAWG_ERROR_UNEXPECTED_RESPONSE =                    (IVIC_ERROR_BASE + 0x0059)
KTMAWG_ERROR_FILE_NOT_FOUND =                         (IVIC_ERROR_BASE + 0x005B)
KTMAWG_ERROR_INVALID_FILE_FORMAT =                    (IVIC_ERROR_BASE + 0x005C)
KTMAWG_ERROR_STATUS_NOT_AVAILABLE =                   (IVIC_ERROR_BASE + 0x005D)
KTMAWG_ERROR_ID_QUERY_FAILED =                        (IVIC_ERROR_BASE + 0x005E)
KTMAWG_ERROR_RESET_FAILED =                           (IVIC_ERROR_BASE + 0x005F)
KTMAWG_ERROR_RESOURCE_UNKNOWN =                       (IVIC_ERROR_BASE + 0x0060)
KTMAWG_ERROR_ALREADY_INITIALIZED =                    (IVIC_ERROR_BASE + 0x0061)
KTMAWG_ERROR_CANNOT_CHANGE_SIMULATION_STATE =         (IVIC_ERROR_BASE + 0x0062)
KTMAWG_ERROR_INVALID_NUMBER_OF_LEVELS_IN_SELECTOR =   (IVIC_ERROR_BASE + 0x0063)
KTMAWG_ERROR_INVALID_RANGE_IN_SELECTOR =              (IVIC_ERROR_BASE + 0x0064)
KTMAWG_ERROR_UNKOWN_NAME_IN_SELECTOR =                (IVIC_ERROR_BASE + 0x0065)
KTMAWG_ERROR_BADLY_FORMED_SELECTOR =                  (IVIC_ERROR_BASE + 0x0066)
KTMAWG_ERROR_UNKNOWN_PHYSICAL_IDENTIFIER =            (IVIC_ERROR_BASE + 0x0067)
KTMAWG_ERROR_INVALID_SESSION_HANDLE =                 (IVIC_ERROR_BASE + 0x1190)



KTMAWG_SUCCESS =                                      0
KTMAWG_WARN_NSUP_ID_QUERY =                           (IVIC_WARN_BASE + 0x0065)
KTMAWG_WARN_NSUP_RESET =                              (IVIC_WARN_BASE + 0x0066)
KTMAWG_WARN_NSUP_SELF_TEST =                          (IVIC_WARN_BASE + 0x0067)
KTMAWG_WARN_NSUP_ERROR_QUERY =                        (IVIC_WARN_BASE + 0x0068)
KTMAWG_WARN_NSUP_REV_QUERY =                          (IVIC_WARN_BASE + 0x0069)



KTMAWG_ERROR_IO_GENERAL =                             (IVIC_SPECIFIC_ERROR_BASE + 0x0214)
KTMAWG_ERROR_IO_TIMEOUT =                             (IVIC_SPECIFIC_ERROR_BASE + 0x0215)
KTMAWG_ERROR_CALIBRATION_VERSION =                    (IVIC_SPECIFIC_ERROR_BASE + 0x0217)
KTMAWG_ERROR_CHECK_ERROR_QUEUE =                      (IVIC_SPECIFIC_ERROR_BASE + 0x0218)
KTMAWG_ERROR_FILE_TYPE_NOT_RECOGNIZED =               (IVIC_SPECIFIC_ERROR_BASE + 0x0219)
KTMAWG_ERROR_FIRMWARE_UPDATE_ERROR =                  (IVIC_SPECIFIC_ERROR_BASE + 0x021A)
KTMAWG_ERROR_FIRMWARE_UPDATE_REQUIRED =               (IVIC_SPECIFIC_ERROR_BASE + 0x021B)
KTMAWG_ERROR_FPGA_PROGRAMMING_ERROR =                 (IVIC_SPECIFIC_ERROR_BASE + 0x021C)
KTMAWG_ERROR_HARDWARE_TIMEOUT =                       (IVIC_SPECIFIC_ERROR_BASE + 0x021D)
KTMAWG_ERROR_HW_RESOURCE_NOT_AVAILABLE =              (IVIC_SPECIFIC_ERROR_BASE + 0x021E)
KTMAWG_ERROR_INCOMPATIBLE_SOFTWARE_VERSION_ERROR =    (IVIC_SPECIFIC_ERROR_BASE + 0x021F)
KTMAWG_ERROR_INSTRUMENT_CALIBRATION_DUE =             (IVIC_SPECIFIC_ERROR_BASE + 0x0220)
KTMAWG_ERROR_INSTRUMENT_CALIBRATION_EXPIRED =         (IVIC_SPECIFIC_ERROR_BASE + 0x0221)
KTMAWG_ERROR_INSTRUMENT_NOT_CALIBRATED =              (IVIC_SPECIFIC_ERROR_BASE + 0x0222)
KTMAWG_ERROR_INTERNAL_APPLICATION_ERROR =             (IVIC_SPECIFIC_ERROR_BASE + 0x0223)
KTMAWG_ERROR_LICENSE_SYSTEM_ERROR =                   (IVIC_SPECIFIC_ERROR_BASE + 0x0224)
KTMAWG_ERROR_LICENSE_VALIDATION_ERROR =               (IVIC_SPECIFIC_ERROR_BASE + 0x0225)
KTMAWG_ERROR_MAX_TIME_EXCEEDED =                      (IVIC_SPECIFIC_ERROR_BASE + 0x0226)
KTMAWG_ERROR_MISSING_CLOCK_ERROR =                    (IVIC_SPECIFIC_ERROR_BASE + 0x0227)
KTMAWG_ERROR_MODEL_NOT_SUPPORTED =                    (IVIC_SPECIFIC_ERROR_BASE + 0x0228)
KTMAWG_ERROR_MODULE_CALIBRATION_DUE =                 (IVIC_SPECIFIC_ERROR_BASE + 0x0229)
KTMAWG_ERROR_MODULE_CALIBRATION_EXPIRED =             (IVIC_SPECIFIC_ERROR_BASE + 0x022A)
KTMAWG_ERROR_MODULE_NOT_CALIBRATED =                  (IVIC_SPECIFIC_ERROR_BASE + 0x022B)
KTMAWG_ERROR_MODULE_VALIDATE_FAILED =                 (IVIC_SPECIFIC_ERROR_BASE + 0x022C)
KTMAWG_ERROR_OPERATION_ABORTED =                      (IVIC_SPECIFIC_ERROR_BASE + 0x022D)
KTMAWG_ERROR_OPERATION_ERROR =                        (IVIC_SPECIFIC_ERROR_BASE + 0x022E)
KTMAWG_ERROR_OUT_OF_MEMORY_ERROR =                    (IVIC_SPECIFIC_ERROR_BASE + 0x022F)
KTMAWG_ERROR_PARAMETER_VALIDATION_ERROR =             (IVIC_SPECIFIC_ERROR_BASE + 0x0230)
KTMAWG_ERROR_PERSONALITY_NOT_ACTIVE =                 (IVIC_SPECIFIC_ERROR_BASE + 0x0231)
KTMAWG_ERROR_PERSONALITY_NOT_INSTALLED =              (IVIC_SPECIFIC_ERROR_BASE + 0x0232)
KTMAWG_ERROR_PERSONALITY_NOT_LICENSED =               (IVIC_SPECIFIC_ERROR_BASE + 0x0233)
KTMAWG_ERROR_SELFTEST_FAILED =                        (IVIC_SPECIFIC_ERROR_BASE + 0x0234)
KTMAWG_ERROR_SOFTWARE_TIMEOUT =                       (IVIC_SPECIFIC_ERROR_BASE + 0x0235)
KTMAWG_ERROR_TEST_FAILED_INCORRECT_VERSION =          (IVIC_SPECIFIC_ERROR_BASE + 0x0236)
KTMAWG_ERROR_THERMAL_SHUTDOWN =                       (IVIC_SPECIFIC_ERROR_BASE + 0x0237)
KTMAWG_ERROR_THERMAL_WARNING =                        (IVIC_SPECIFIC_ERROR_BASE + 0x0238)
KTMAWG_ERROR_UNABLE_TO_INITIALIZE_HARDWARE =          (IVIC_SPECIFIC_ERROR_BASE + 0x0239)
KTMAWG_ERROR_UNRECOGNIZED_ERROR =                     (IVIC_SPECIFIC_ERROR_BASE + 0x023A)
KTMAWG_ERROR_UNSUPPORTED_FEATURE =                    (IVIC_SPECIFIC_ERROR_BASE + 0x023B)
KTMAWG_ERROR_UNSUPPORTED_PROPERTY =                   (IVIC_SPECIFIC_ERROR_BASE + 0x023C)
KTMAWG_ERROR_VALIDATION_ERROR =                       (IVIC_SPECIFIC_ERROR_BASE + 0x023D)
KTMAWG_ERROR_VERIFY_OPERATION_ERROR =                 (IVIC_SPECIFIC_ERROR_BASE + 0x023E)
KTMAWG_ERROR_WAIT_ABORTED =                           (IVIC_SPECIFIC_ERROR_BASE + 0x023F)
KTMAWG_ERROR_TRIGGER_NOT_SOFTWARE =                   (IVIC_CLASS_ERROR_BASE + 0x0001)
KTMAWG_ERROR_NO_WFMS_AVAILABLE =                      (IVIC_CLASS_ERROR_BASE + 0x0004)
KTMAWG_ERROR_WFM_IN_USE =                             (IVIC_CLASS_ERROR_BASE + 0x0008)
KTMAWG_ERROR_NO_SEQS_AVAILABLE =                      (IVIC_CLASS_ERROR_BASE + 0x0009)
KTMAWG_ERROR_SEQ_IN_USE =                             (IVIC_CLASS_ERROR_BASE + 0x000D)
KTMAWG_ERROR_INVALID_WFM_CHANNEL =                    (IVIC_CLASS_ERROR_BASE + 0x000E)
KTMAWG_ERROR_COMPILATION_ERROR =                      (IVIC_SPECIFIC_ERROR_BASE + 0x0240)
KTMAWG_ERROR_HARDWARE_STATE_ERROR =                   (IVIC_SPECIFIC_ERROR_BASE + 0x0241)
KTMAWG_ERROR_INCONSISTENT_MULTI_CHANNEL_PROPERTY =    (IVIC_SPECIFIC_ERROR_BASE + 0x0242)
KTMAWG_ERROR_INVALID_PARAMETER =                      (IVIC_SPECIFIC_ERROR_BASE + 0x0243)
KTMAWG_ERROR_MODULE_OUT_OF_MEMORY =                   (IVIC_SPECIFIC_ERROR_BASE + 0x0245)
KTMAWG_ERROR_SETTINGS_CONFLICT =                      (IVIC_SPECIFIC_ERROR_BASE + 0x0246)



KTMAWG_WARN_VALIDATION_FAILED =                       (IVIC_SPECIFIC_WARN_BASE + 0x012D)
