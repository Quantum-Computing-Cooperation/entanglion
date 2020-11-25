using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class GameManager : NetworkBehaviour
{
    public string[] qcPlanets = new string[]{ "PSI_PLUS", "PSI_MINUS", "PHI_PLUS", "PHI_MINUS", "OMEGA_ONE",  "OMEGA_TWO", "OMEGA_THREE",  "OMEGA_ZERO" };
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

    public void ShuffleQcPlanets()
    {
        System.Random random = new System.Random();
        for (int i = qcPlanets.Length - 1; i > 0; i--)
        {
            int randomIndex = random.Next(0, i + 1);
            string temp = qcPlanets[i];
            qcPlanets[i] = qcPlanets[randomIndex];
            qcPlanets[randomIndex] = temp;
        }
    }
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
