#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from qcodes import Instrument, Parameter
from qcodes.utils.validators import Numbers, Bool, Enum

def key_of_val(dictionary, val):
    return list(dictionary.keys())[list(dictionary.values()).index(val)]

class CA5350(Instrument):
    '''
    koko motto kireini shitakatta kedo dekinakatta node hitsuyou dattara onegaishimasu

    bias_on (bool)     : Whether you apply bias voltage or not. Default = False.
    bias_voltage(-8~8) : Bias voltage.

    total_gain                                         : Read only. Total gain as result of IV_gain and post_gain.
    IV_gain (10e3, 100e3, 1e6, 10e6, 100e6, 1e9, 10e9) : I/V gain. Default = 10e3. 
    post_gain (1(=*1), 10(=*10))                       : Post amplifier gain. Default = 1. 
    
    suppression_on (False, True, 'auto'(mauto suppression start)): Whether you use suppression. Default = False. 
    auto_suppression_range_on (bool)                             : Whether you decide suppression range automatically. Default = False. Note that this is different from suppression_on.
    suppression_range (8e-9(resolution = 1pA), 80e-9(10pA), 800e-9(100pA), 8e-6(1nA), 80e-6(10nA), 800e-6(100nA)): You can decide suppression range manually. Units = A. Default = 800e-6.
    
    filter_on(bool)             : Whether you use filter. Default = False.
    auto_filter_on (bool)       : Whether you decide filter rise time automatically. Note that this is differnt from filter_on.
    filter_rise (1e-6, 3e-6, 10e-6, 30e-6, 100e-6, 300e-6, 1e-3, 3e-3, 10e-3, 30e-3, 100e-3, 300e-3): You can decide filter rise time manually. Units = seconds. Default = 10e-6.

    zero_check (bool)                  : Check dark current. Default = False. Turn on this and calibrate suppression can cancel offset.
    backlight('max', 'medium', 'OFF')  : You can change backlight brightness of LCD.
    input_fr('front', 'rear')          : You can change current input connecter of front or rear pannel. Default = 'front'.
    diagnosis                          : Read only. Check diagnosis results.
    memory_test                        : Read only. Memory test.
    message                            : You can display some message on LCD. Calling this function without any args delete desplayed message.
    '''
    def __init__(self, name, address, **kwargs):
        super().__init__(name, **kwargs)
        self.address = address
        self.re_num = re.compile(r'[0-9./]+')
        self.corresp_dict = {
            'backlight': 'A',
            'bias_on': 'B',
            'zero_check': 'C',
            'input_fr': 'I',
            'diagnosis': 'J',
            'suppression_on': 'N',
            'filter_on': 'P',
            'IV_gain': 'R',
            'auto_suppression_range_on': 'S',
            'suppression_range': 'S',
            'filter_rise': 'T',
            'post_gain': 'W',
            'auto_filter_on': 'Z'
        }
        self.backlight_dict = {'0': 'max', '1': 'medium', '2': 'OFF'}
        self.bias_on_dict = {'0': False, '1': True}
        self.zero_check_dict = {'0': False, '1': True}
        self.input_fr_dict = {'0': 'front', '1': 'rear'}
        self.diagnosis_dict = {
            '0': 'good',
            '1': 'ROM error',
            '2': 'RAM error',
            '3': 'ROM and RAM error',
            '4': 'NVRAM error'
        }
        self.suppression_on_dict = {'0': False, '1': True, '2': 'auto'}
        self.filter_on_dict = {'0': False, '2': True}
        self.IV_gain_dict = {
            '04': 10e3, '05': 100e3, '06': 1e6, '07': 10e6, 
            '08': 100e6, '09': 1e9, '10': 10e9
        }
        self.auto_suppression_range_on_dict = {'0': False, '1': True}
        self.suppression_range_dict = {
            '1': 8e-9, '2': 80e-9, '3': 800e-9, '4': 8e-6, '5': 80e-6, '6': 800e-6
        }
        self.filter_rise_dict = {
            '.': 1e-6, '/': 3e-6, '0': 10e-6, '1': 30e-6, '2': 100e-6, 
            '3': 300e-6, '4': 1e-3, '5': 3e-3, '6': 10e-3, '7': 30e-3, 
            '8': 100e-3, '9': 300e-3
        }
        self.post_gain_dict = {'0': 1, '1': 10}
        self.auto_filter_on_dict = {'0': False, '1': True}

        # Parameters
        self.add_parameter(
            'bias_on',
            label='Bias On',
            get_cmd=self._get_bias_on,
            set_cmd=self._set_bias_on,
            vals=Bool()
        )
        
        self.add_parameter(
            'bias_voltage',
            label='Bias Voltage',
            unit='V',
            get_cmd=self._get_bias_voltage,
            set_cmd=self._set_bias_voltage,
            vals=Numbers(-8, 8)
        )

        self.add_parameter(
            'total_gain',
            label='Total Gain',
            get_cmd=self._get_total_gain,
            unit='dB'
        )

        self.add_parameter(
            'IV_gain',
            label='IV Gain',
            get_cmd=self._get_IV_gain,
            set_cmd=self._set_IV_gain,
            vals=Enum(*self.IV_gain_dict.values())
        )

        self.add_parameter(
            'post_gain',
            label='Post Gain',
            get_cmd=self._get_post_gain,
            set_cmd=self._set_post_gain,
            vals=Enum(*self.post_gain_dict.values())
        )

        self.add_parameter(
            'suppression_on',
            label='Suppression On',
            get_cmd=self._get_suppression_on,
            set_cmd=self._set_suppression_on,
            vals=Enum(False, True, 'auto')
        )

        self.add_parameter(
            'filter_on',
            label='Filter On',
            get_cmd=self._get_filter_on,
            set_cmd=self._set_filter_on,
            vals=Bool()
        )

    # Getters and setters
    def _get_bias_on(self):
        return self.bias_on_dict.get(self.ask('B?'))

    def _set_bias_on(self, value):
        self.write(f'B{key_of_val(self.bias_on_dict, value)}X')

    def _get_bias_voltage(self):
        return float(self.ask('U2X')[1:8])

    def _set_bias_voltage(self, value):
        self.write(f'V{value:.3f}X')

    def _get_total_gain(self):
        return float('10e' + self.ask('U3X')[2:4])

    def _get_IV_gain(self):
        return self.IV_gain_dict.get(self.ask('R?'))

    def _set_IV_gain(self, value):
        self.write(f'R{key_of_val(self.IV_gain_dict, value)}X')

    def _get_post_gain(self):
        return self.post_gain_dict.get(self.ask('W?'))

    def _set_post_gain(self, value):
        self.write(f'W{key_of_val(self.post_gain_dict, value)}X')

    def _get_suppression_on(self):
        return self.suppression_on_dict.get(self.ask('N?'))

    def _set_suppression_on(self, value):
        self.write(f'N{key_of_val(self.suppression_on_dict, value)}X')

    def _get_filter_on(self):
        return self.filter_on_dict.get(self.ask('P?'))

    def _set_filter_on(self, value):
        self.write(f'P{key_of_val(self.filter_on_dict, value)}X')


# In[2]:





# In[ ]:




