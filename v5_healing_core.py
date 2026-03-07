def v5_monitoring_and_healing(conductivity_loss, structural_strain):
    """
    SOMA V5: Self-Healing & Degradation Management
    監控導電率下降與結構應變，判斷是否進入「自癒模式」。
    """
    healing_threshold = 0.15  # 15% 導電率損失觸發預警
    
    if conductivity_loss > healing_threshold:
        # 啟動自癒脈衝：低頻、高占空比，局部溫升到 42.0°C
        healing_pulse_mode = True
        maintenance_temp = 42.0 
        # 恢復效率預估 (Time Constant Tau)
        healing_rate = 1.0 - np.exp(-0.05 * structural_strain)
    else:
        healing_pulse_mode = False
        maintenance_temp = 37.5
        
    return healing_pulse_mode, maintenance_temp
