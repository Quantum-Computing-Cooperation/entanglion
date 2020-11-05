using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EngineControl : MonoBehaviour
{

    public int nSlot;
    private readonly float dx = 960;
    private readonly float dy = 540;
    // Update is called once per frame
    void Update()
    {
        PlaceToken(nSlot);
    }
    void PlaceToken(int placement)
    {
        switch (placement)
        {
            case 0:
                this.transform.position = new Vector2(-144 + dx, 463 + dy);
                break;
            case 1:
                this.transform.position = new Vector2(27 + dx, 463 + dy);
                break;
            case 2:
                this.transform.position = new Vector2(198 + dx, 463 + dy);
                break;
            case 3:
                this.transform.position = new Vector2(367.5f + dx, 463 + dy);
                break;
            case 4:
                this.transform.position = new Vector2(538 + dx, 463 + dy);
                break;
            case 5:
                this.transform.position = new Vector2(709 + dx, 463 + dy);
                break;
            default:
                break;
        }
    }

}
