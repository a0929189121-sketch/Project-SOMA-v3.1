"""
Project S.O.M.A. - V4 [The Mechanical Soul] 
Core Logic & Actuation Controller (Open Source Version)
Developed by S.O.M.A. Central R&D Hub
"""

import math

class SOMA_V4_Controller:
    def __init__(self):
        self.lock_force_max = 3125.0  # Newton (N)
        self.success_points = 7520    # Initial Safety Points
        self.fluid_viscosity = 1.0    # Fluid Viscosity Factor
        self.contract_100y_active = True

    def calculate_hydraulic_compensation(self, target_force, ambient_temp):
        """
        蜘蛛液壓耦合補償算法 (Spider-Hydraulic Compensation)
        根據環境溫度調整黏度修正因子 f(eta)
        """
        # 黏度修正公式 f(eta) = e^(-0.03 * (temp - 25))
        viscosity_correction = math.exp(-0.03 * (ambient_temp - 25))
        required_pump_pressure = (target_force / self.lock_force_max) * viscosity_correction
        
        return min(required_pump_pressure, 1.0) # 限制最大壓力輸出

    def process_tactile_feedback(self, fsr_matrix_data):
        """
        觸覺感測濾波 (Tactile Matrix Filtering)
        區分愛撫 (Low Freq) 與 衝擊 (High Freq)
        """
        # 這裡未來應接入 FFT (快速傅立葉變換)
        frequency = sum(fsr_matrix_data) / len(fsr_matrix_data)
        
        if frequency < 5.0:
            return "GENTLE_TOUCH"
        elif frequency > 50.0:
            self.trigger_shadow_protocol()
            return "IMPACT_DETECTED"
        return "NORMAL_CONTACT"

    def trigger_shadow_protocol(self):
        """
        影子對策 (Shadow Protocol)
        當偵測到危險或異常時，強制降低液壓出力至安全閾值
        """
        print("[WARNING] Shadow Protocol Engaged: Limiting Output to 25N.")
        self.current_output_limit = 25.0

# 實例化 V4 控制核心
soma_v4 = SOMA_V4_Controller()
