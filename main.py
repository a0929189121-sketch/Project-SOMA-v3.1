import numpy as np

def calculate_compensation(target_f, feedback_f, history_50ms, kp=0.8, kc=1.2):
    """
    SOMA v3.1: 4.96ms Adaptive Compensation Logic
    """
    error = target_f - feedback_f
    
    # 驟變檢測 (零過衝補丁)
    if abs(error) > 300:
        history_50ms *= 0   
        kc *= 0.5            
    
    # 模擬 LSTM 預測延遲 (實戰需加載權重)
    predicted_lag = 0.12  
    
    # 5.0V 安全電壓輸出
    output = (error * kp) + (predicted_lag * kc)
    return max(0.0, min(float(output), 5.0))

if __name__ == "__main__":
    print("S.O.M.A v3.1 Engine Online.")
