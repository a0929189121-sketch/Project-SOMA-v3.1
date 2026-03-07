"""
Project S.O.M.A. - V6 [Neural Synapse]
Module: Distributed Reflex Arc & Synaptic Weighting
Logic: Non-Centralized Reaction for Edge Processing
"""

class SOMA_V6_Synapse:
    def __init__(self):
        self.synaptic_weight = 1.0  # 感知靈敏度權重 (1.0 to 10.0)
        self.reflex_threshold = 0.85 # 反射觸發閾值
        self.last_input_pattern = []

    def compute_reflex_arc(self, local_pressure_delta):
        """
        邊緣反射弧 (Edge Reflex Arc)
        跳過中央決策，直接由局部控制單元執行保護性撤回
        """
        # 模擬神經元快速去極化
        activation_potential = local_pressure_delta * self.synaptic_weight
        
        if activation_potential > self.reflex_threshold:
            print("[REFLEX] Local Synapse Fired: Immediate Retraction Executed.")
            return "RETRACT_ACTION"
        return "IDLE"

    def update_synaptic_plasticity(self, interaction_frequency):
        """
        神經可塑性 (Plasticity)
        根據互動頻率調整權重，實現「越互動越靈敏」或「習慣化」
        """
        # 模擬突觸長時程增益 (LTP)
        self.synaptic_weight += (interaction_frequency * 0.05)
        self.synaptic_weight = min(self.synaptic_weight, 10.0)
        print(f"--- Synaptic Weight Updated: {self.synaptic_weight:.2f} ---")

    def fuse_sensory_data(self, hydraulic_p, tactile_f, ionic_m):
        """
        多模態感知融合 (Sensor Fusion)
        整合液壓(P)、觸覺(F)、離子肌肉電流(M) 形成空間感
        """
        # 空間坐標映射邏輯
        perception_vector = (hydraulic_p * 0.4) + (tactile_f * 0.4) + (ionic_m * 0.2)
        return perception_vector
