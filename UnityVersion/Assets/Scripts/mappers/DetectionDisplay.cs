using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DetectionDisplay : MonoBehaviour
{

    public int rate;
    private readonly float dx = 960;
    private readonly float dy = 540;
    // Update is called once per frame
    void Update()
    {
        PlaceToken(rate);
    }
    void PlaceToken(int placement)
    {
        switch (placement)
        {
            case 0:
                this.transform.position = new Vector2(-908 + dx, 220 + dy);
                break;
            case 1:
                this.transform.position = new Vector2(-855.5f + dx, 220 + dy);
                break;
            case 2:
                this.transform.position = new Vector2(-803 + dx, 220 + dy);
                break;
            case 3:
                this.transform.position = new Vector2(-750.5f + dx, 220 + dy);
                break;
            case 4:
                this.transform.position = new Vector2(-698 + dx, 220 + dy);
                break;
            case 5:
                this.transform.position = new Vector2(-645.5f + dx, 220 + dy);
                break;
            case 6:
                this.transform.position = new Vector2(-881.5f + dx, 181.5f + dy);
                break;
            case 7:
                this.transform.position = new Vector2(-829 + dx, 181.5f + dy);
                break;
            case 8:
                this.transform.position = new Vector2(-776.5f + dx, 181.5f + dy);
                break;
            case 9:
                this.transform.position = new Vector2(-724 + dx, 181.5f + dy);
                break;
            case 10:
                this.transform.position = new Vector2(-671.5f + dx, 181.5f + dy);
                break;
            case 11:
                this.transform.position = new Vector2(-619 + dx, 181.5f + dy);
                break;
            default:
                break;
        }
    }

}
