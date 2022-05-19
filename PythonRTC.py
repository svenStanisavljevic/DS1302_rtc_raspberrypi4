#!/usr/bin/python
#coding=utf-8
# PythonRTC - Python Hardware Programming Education Project For Raspberry Pi
# Copyright (C) 2015 Jason Birch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#/****************************************************************************/
#/* PythonRTC                                                                */
#/* ------------------------------------------------------------------------ */
#/* V1.00 - 2015-08-26 - Jason Birch                                         */
#/* V2.00 - 2021-03-20 - Sven Stanisavljević                                 */
#/* ------------------------------------------------------------------------ */
#/* Example of using class to handle controlling a Real Time Clock IC DS1302.*/
#/****************************************************************************/

import RTC_DS1302
import sys

def main(argv):
    
    #Create an instance of the RTC class.
    ThisRTC = RTC_DS1302.RTC_DS1302()
    #Functions to write to the RTC chip.
    if len(argv) > 1:
        ThisRTC.WriteDateTime((int(argv[0]) - 2000), int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5]), int(argv[6]))

    DateTime = { "Year":0, "Month":0, "Day":0, "DayOfWeek":0, "Hour":0, "Minute":0, "Second":0 }
    Data = ThisRTC.ReadDateTime(DateTime)
    print(Data)

    #Finish with the Raspberry Pi GPIO pins.
    ThisRTC.CloseGPIO()
    
if __name__ == "__main__":
    main(sys.argv[1:])
