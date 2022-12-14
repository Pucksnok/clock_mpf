from mpf.core.mode import Mode
import time
import logging


class GetClock(Mode):
    def mode_start(self, **kwargs):
           # del kwargs
            self.add_mode_event_handler('set_clock', self._write_time)
    
    def _write_time(self, **kwargs):
            time_string = time.strftime("%H:%M") # %H:%M for Hour and Minutes, can change to whatever you need.
            self.machine.variables.set_machine_var("time_variable", time_string) 
            self.machine.events.post("time_variable_saved")





