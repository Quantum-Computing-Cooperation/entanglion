using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class GameManager : NetworkBehaviour
{
    public UIManager uiManager;
    [HideInInspector]
    public int nRolls = 0;
    [HideInInspector]
    public int myRoll;
    [HideInInspector]
    public int hisRoll;
    [HideInInspector]
    public string gameState = "Initialize {}";
    [HideInInspector]
    public bool isMyTurn = false;


    public void ChangeGameState(string stateRequest)
    {
        if(stateRequest == "Initialize {}")
        {
            nRolls = 0;
            gameState = "Initialize {}";

        }else if (stateRequest == "Compile {}")
        {
            if(nRolls == 1)
            {
                if (hisRoll == myRoll)
                {
                    gameState = "Compile {Draw}";
                }
                else if(myRoll > hisRoll)
                {
                    gameState = "Compile {Higher}";
                    isMyTurn = true;

                }
                else
                {
                    gameState = "Compile {Lower}";
                    isMyTurn = false;
                }
            }
        }else if (stateRequest == "Execute {}")
        {
            gameState = "Execute {}";
        }
    }

    public void ChangeRolls(int roll, bool hasAuthority)
    {
        if (hasAuthority)
        {
            myRoll = roll;
        }
        else
        {
            hisRoll = roll;
        }
        nRolls++;
    }

}
