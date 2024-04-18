from simple_pid import PID
from mpu6050 import mpu6050
from gpiozero import OutputDevice
from servo import Servo
from time import sleep

def gpz_init():
	gpio = OutputDevice(5)
	gpio.off()
	sleep(0.01)
	gpio.on()
	sleep(0.01)
	gpio.close()

def main():
	Kp, Ki, Kd = 1, 0, 0
	setpointx, setpointy = 0, 0
	sample_time = 0.01
	pidx = PID(Kp, Ki, Kd, setpointx, sample_time)
	pidy = PID(Kp, Ki, Kd, setpointy, sample_time)
	mpu = mpu6050(0x68)	
	svop = Servo("P0")		# yaw	- y
	svot = Servo("P1") 		# pitch	- x
	t = 0.5
	svop.angle(setpointy)
	sleep(t)
	svot.angle(setpointx)
	sleep(t)
	while True:
		gyro_data = mpu.get_gyro_data()
		gx = round(gyro_data['x'], 4)
		gy = round(gyro_data['y'], 4)
		print("observation: gyro (x, y): ", gx, gy)

		day = pidx(gx)
		dax = pidy(gy)
		print("expected changes: angle (x, y): ", dax, day)

		svop.angle(day)
		sleep(t)
		svot.angle(dax)
		sleep(t)

if __name__ == "__main__":
	gpz_init()
	main()
