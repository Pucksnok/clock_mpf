from mpf.core.mode import Mode
import time
import logging


class GetClock(Mode):
    def mode_start(self, **kwargs):
           # del kwargs
            self.add_mode_event_handler('set_clock', self._write_time)
            self.add_mode_event_handler('set_date', self._write_date)
    
    def _write_time(self, **kwargs):
            time_string = time.strftime("%H:%M")
            self.machine.variables.set_machine_var("time_variable", time_string) 
            self.machine.events.post("time_variable_saved")
    def _write_date(self, **kwargs):
            time_string = time.strftime("20%y.%m.%d")
            self.machine.variables.set_machine_var("date_variable", time_string) 
            self.machine.events.post("date_variable_saved")




