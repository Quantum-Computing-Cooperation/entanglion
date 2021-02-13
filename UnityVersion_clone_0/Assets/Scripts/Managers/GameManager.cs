using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class GameManager : NetworkBehaviour
{
    public string[] qcPlanets;
    public UIManager uiManager;
    [HideInInspector]
    public int nPlanetRolls;
    [HideInInspector]
    public int nRolls;
    [HideInInspector]
    public int myRoll;
    [HideInInspector]
    public int hisRoll;
    public string gameState;
    public bool isMyTurn;
    public string shipPlanet;

    private void Start()
    {
        nRolls = 0;
        nPlanetRolls = 0;
        qcPlanets = new string[] { "PSI_PLUS", "PSI_MINUS", "PHI_PLUS", "PHI_MINUS", "OMEGA_ONE", "OMEGA_TWO", "OMEGA_THREE", "OMEGA_ZERO" };
        gameState = "Initialize {}";
        isMyTurn = false;
        shipPlanet = "ZERO";
    }

    public void changeTurn()
    {
        isMyTurn = !isMyTurn;
    }

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
            nPlanetRolls = 0;
            if(nRolls == 2)
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
            nPlanetRolls++;
            if (nPlanetRolls == 2)
            {
                gameState = "Execute {}";
            }

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
