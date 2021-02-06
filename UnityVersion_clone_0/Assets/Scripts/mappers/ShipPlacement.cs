using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShipPlacement : MonoBehaviour
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
            case "ONE":
                this.transform.position = new Vector2(-167 + dx,107 + dy);
                break;
            case "ZERO":
                this.transform.position = new Vector2(-90 + dx, -108 + dy);
                break;
            case "PSI_PLUS":
                this.transform.position = new Vector2(157 + dx, 106 + dy);
                break;
            case "PSI_MINUS":
                this.transform.position = new Vector2(715 + dx, 108 + dy);
                break;
            case "PHI_PLUS":
                this.transform.position = new Vector2(157 + dx, -112 + dy);
                break;
            case "PHI_MINUS":
                this.transform.position = new Vector2(715 + dx, -115 + dy);
                break;
            case "OMEGA_ONE":
                this.transform.position = new Vector2(566 + dx, 273 + dy);
                break;
            case "OMEGA_TWO":
                this.transform.position = new Vector2(312 + dx, -262 + dy);
                break;
            case "OMEGA_THREE":
                this.transform.position = new Vector2(569 + dx, -262 + dy);
                break;
            case "OMEGA_ZERO":
                this.transform.position = new Vector2(305 + dx, 273 + dy);
                break;
            case "MINUS":
                this.transform.position = new Vector2(709 + dx, -442 + dy);
                break;
            case "PLUS":
                this.transform.position = new Vector2(160 + dx, -362 + dy);
                break;
            default:
                break;
        }
    }
}
