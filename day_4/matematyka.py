import math

print(math.pi)  # 3.141592653589793

print(math.sqrt(25))  # 5.0

angle_degrees = 30
angle_radians = math.radians(angle_degrees)
sin_value = math.sin(angle_radians)

print(f"sin({angle_degrees}°) = {sin_value}")
# sin(30°) = 0.49999999999999994

angles = [0, 30, 45, 60, 90]
sin_values = [math.sin(math.radians(a)) for a in angles]

for a, s in zip(angles, sin_values):
    print(f"sin({a}°) = {s}")
# sin(0°) = 0.0
# sin(30°) = 0.49999999999999994
# sin(45°) = 0.7071067811865476
# sin(60°) = 0.8660254037844386
# sin(90°) = 1.0
