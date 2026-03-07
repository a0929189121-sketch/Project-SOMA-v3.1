import numpy as np

class SOMAV4Engine:
    def __init__(self):
        self.temp_target = 37.5          # 目標溫度
        self.resonance_freq = 124.5      # 結構共振點 (Hz)
        self.fluid_pressure = 1.0        # 流體壓力 (Bar)
        
    def adaptive_control(self, error, current_temp, freq):
        # 1. 熱補償：溫度漂移校正
        thermal_gain = 1.0 / (1.0 + 0.03 * (current_temp - self.temp_target))
        
        # 2. 諧振消除：反相脈衝
        if abs(freq - self.resonance_freq) < 5.0:
            anti_resonance_pulse = -0.15 * np.sin(2 * np.pi * freq)
        else:
            anti_resonance_pulse = 0
            
        # 3. 最終輸出
        v_out = (error * 0.85 * thermal_gain) + anti_resonance_pulse
        
        # 5V 安全截斷
        return np.clip(v_out, 0.0, 5.0)
