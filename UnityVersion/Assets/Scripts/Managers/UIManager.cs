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
    public GameObject[] components;
    // Start is called before the first frame update
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
