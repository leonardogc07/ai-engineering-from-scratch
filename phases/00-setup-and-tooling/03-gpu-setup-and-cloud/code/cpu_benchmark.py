import torch
import time

size = 5000
a = torch.randn(size, size)
b = torch.randn(size, size)

start = time.time()
c = a @ b
cpu_time = time.time() - start
print(f"CPU time: {cpu_time:.3f} seconds")

device = torch.device("mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu")
a = a.to(device)
b = b.to(device)

if device.type == "mps":
    torch.mps.synchronize()
elif device.type == "cuda":
    torch.cuda.synchronize()

start = time.time()
c = a @ b
if device.type == "mps":
    torch.mps.synchronize()
elif device.type == "cuda":
    torch.cuda.synchronize()
gpu_time = time.time() - start

print(f"{device} time: {gpu_time:.3f} seconds")
print(f"🚀 Speedup: {cpu_time / gpu_time:.1f}x")