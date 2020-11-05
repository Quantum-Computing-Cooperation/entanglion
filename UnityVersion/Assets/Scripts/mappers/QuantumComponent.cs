using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QuantumComponent : MonoBehaviour
{
    public string planet;
    private readonly float dx = 960;
    private readonly float dy = 540;
    private void Update()
    {
        PlaceShip(planet);
    }
    void PlaceShip(string planet)
    {
        switch (planet)
        {
            case "PSI_PLUS":
                this.transform.position = new Vector2(163.5f + dx, 104 + dy);
                break;
            case "PSI_MINUS":
                this.transform.position = new Vector2(713 + dx, 104 + dy);
                break;
            case "PHI_PLUS":
                this.transform.position = new Vector2(163.5f + dx, -112 + dy);
                break;
            case "PHI_MINUS":
                this.transform.position = new Vector2(714.8f + dx, -113.8f + dy);
                break;
            case "OMEGA_ONE":
                this.transform.position = new Vector2(571.1f + dx, 269.2f + dy);
                break;
            case "OMEGA_TWO":
                this.transform.position = new Vector2(315.1f + dx, -262.8f + dy);
                break;
            case "OMEGA_THREE":
                this.transform.position = new Vector2(572.6f + dx, -264.7f + dy);
                break;
            case "OMEGA_ZERO":
                this.transform.position = new Vector2(313.7f + dx, 269.2f + dy);
                break;
            default:
                break;
        }
    }
}
