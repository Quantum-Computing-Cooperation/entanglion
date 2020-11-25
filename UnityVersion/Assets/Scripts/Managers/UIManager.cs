using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;
using UnityEngine.UI;

public class UIManager : NetworkBehaviour
{
    public GameManager gameManager;
    public GameObject rollText;
    public GameObject rollButton;
    // Start is called before the first frame update

    enum QuantumOrder : ushort
    {
        ControlInfrastructure = 0,
        DillutionRefrigerator = 1,
        MagneticShielding = 2,
        PhysicalQubits = 3,
        QuantumErrorCorrection = 4,
        QuantumGates = 5,
        QuantumProgramming = 6,
        QubitInterconnect = 7,
        COMPONENTS_LENGTH = 8
    }
    private void Start()
    {
        gameManager = GameObject.Find("UIManager").GetComponent<GameManager>();
        rollText.GetComponent<Text>().text = "";
    }


    public void UpdateRollText(int myRoll, int hisRoll)
    {
        if (myRoll == hisRoll)
        {
            rollText.GetComponent<Text>().text = "YOU BOTH GOT THE SAME SCORE! PLEASE REROLL";
            rollButton.GetComponent<StartRoll>().wasClicked = false;
        }  else if (myRoll > hisRoll)
        {
            rollText.GetComponent<Text>().text = "YOU GOT THE HIGHER ROLL WITH: " + (myRoll + 1) + ". YOU GO FIRST!";
        }
        else
        {
            rollText.GetComponent<Text>().text = "THE OTHER PLAYER GOT THE HIGHER ROLL WITH: " + (hisRoll + 1) + ". THE OTHER PLAYER GOES FIRST!";
        }
    }

    public void displayQc(string[] qcLocations)
    {

    }


}
