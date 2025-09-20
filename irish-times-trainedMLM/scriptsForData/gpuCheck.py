import torch
print(torch.cuda.is_available())  # true
print(torch.cuda.current_device())  # gpu id or 0
print(torch.cuda.get_device_name(0))  # gpu name
#just checking if my gpu is alive and well