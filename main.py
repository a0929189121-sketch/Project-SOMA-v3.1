"""
Project S.O.M.A. - Main Entry Point
Current Version: V4 [The Mechanical Soul]
Integration: Linking V3.1 Hardware to V4 Logic Layer
"""

from Source.SOMA_V4_Core_Logic import SOMA_V4_Controller

def main():
    # 1. 初始化 V4 核心邏輯
    soma_v4 = SOMA_V4_Controller()
    
    print("--- S.O.M.A. V4 [The Mechanical Soul] System Booting ---")
    print(f"Contract 100Y Status: {'ACTIVE' if soma_v4.contract_100y_active else 'OFFLINE'}")
    print(f"Current Safety Points: {soma_v4.success_points}")

    # 2. 模擬環境數據 (例如：民雄研發中心的室溫)
    ambient_temp = 28.5  # 攝氏度
    target_force = 1500.0 # 需求出力 (N)

    # 3. 執行 V4 級別的液壓補償計算
    pressure_output = soma_v4.calculate_hydraulic_compensation(target_force, ambient_temp)
    
    print(f"\n[Environment] Temperature: {ambient_temp}°C")
    print(f[Actuation] Target: {target_force}N | Pump Pressure Output: {pressure_output:.2%}")

    # 4. 觸覺感應測試 (模擬矩陣訊號)
    mock_fsr_data = [1.2, 0.5, 2.1, 0.8] # 模擬輕微觸碰
    touch_type = soma_v4.process_tactile_feedback(mock_fsr_data)
    print(f"[Sensory] Interaction Mode: {touch_type}")

if __name__ == "__main__":
    main()
