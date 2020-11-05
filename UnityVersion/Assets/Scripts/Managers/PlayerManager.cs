using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;
using UnityEngine.UI;


public class PlayerManager : NetworkBehaviour
{

    //other managers
    public UIManager uiManager;
    public GameManager gameManager;

    //all cards gameobjects
    public GameObject[] die = new GameObject[8];
    public GameObject card1;
    public GameObject card2;
    List<GameObject> cards = new List<GameObject>();


    //Gameobject References
    GameObject dice;
    List<GameObject> dieReferences = new List<GameObject>();

    //zones
    public GameObject player1Area;
    public GameObject player2Area;
    public GameObject dropZone;
    public GameObject dieArea;
    public GameObject otherDieArea;

    //Buttons
    public GameObject rollButton;
    public GameObject startGameButton;


    public override void OnStartClient()
    {
        base.OnStartClient();
        player1Area = GameObject.Find("Player1Area");
        player2Area = GameObject.Find("Player2Area");
        dropZone = GameObject.Find("DropZone");
        dieArea = GameObject.Find("DieArea");
        otherDieArea = GameObject.Find("OtherDieArea");
        gameManager = GameObject.Find("GameManager").GetComponent<GameManager>();
        uiManager = GameObject.Find("UIManager").GetComponent<UIManager>();
        rollButton = GameObject.Find("RollButton");
        startGameButton = GameObject.Find("StartGameButton");
        rollButton.GetComponent<StartRoll>().wasClicked = false;
        gameManager.gameState = "Initialize {}";
}

    [Server]
    public override void OnStartServer()
    {
        startGameButton.SetActive(true);
        cards.Add(card1);
        cards.Add(card2);
    }

    [Command]
    public void CmdDealCards()
    {
            GameObject card = Instantiate(cards[Random.Range(0,cards.Count)], new Vector2(0, 0), Quaternion.identity);
            NetworkServer.Spawn(card, connectionToClient);
            RpcShowCard(card, "Dealt");
    }

    [Command]
    public void CmdRollDie()
    {
        int rand = Random.Range(0, die.Length);
        GameObject dice = Instantiate(die[rand], new Vector2(0, 0), Quaternion.identity);
        NetworkServer.Spawn(dice, connectionToClient);
        this.dieReferences.Add(dice);
        RpcShowDie(dice, rand);
        RpcGMChangeState("Compile {}");

        if (gameManager.gameState == "Compile {Draw}")
        {
            RpcShowRollResults();
            rollButton.GetComponent<StartRoll>().wasClicked = false;
            CmdDestroyDie();
            Debug.Log("Tie");
        }
        if(gameManager.gameState == "Compile {Higher}")
        {
            RpcShowRollResults();
            RpcHideRollAndShowStart();
            Debug.Log("HIGHER");

        }
        if(gameManager.gameState == "Compile {Lower}")
        {
            RpcShowRollResults();
            RpcHideRollAndShowStart();
            Debug.Log("lower");
        }
    }


    public void PlayCard(GameObject card) => CmdPlayCard(card);

    [Command]
    void CmdPlayCard(GameObject card) => RpcShowCard(card, "Played");

    [ClientRpc]
    void RpcHideRollAndShowStart()
    {
        rollButton.SetActive(false);
        startGameButton.SetActive(true);
    }
    [ClientRpc]
    void RpcShowCard(GameObject card, string type)
    {
        if(type == "Dealt")
        {
            if (hasAuthority)
            {
                card.transform.SetParent(player1Area.transform, false);
            }
            else
            {
                card.transform.SetParent(player2Area.transform, false);
            }
        }
        else if (type == "Played")
        {
            card.transform.SetParent(dropZone.transform, false);
        }
    }

    [ClientRpc]
    void RpcShowDie(GameObject dice, int rand)
    {
        gameManager.ChangeRolls(rand, hasAuthority);
        if (hasAuthority)
        {
            dice.transform.SetParent(dieArea.transform, false);
        }
        else
        {
            dice.transform.SetParent(otherDieArea.transform, false);
        }

    }

    [ClientRpc]
    void RpcGMChangeState(string stateRequest)
    {
        gameManager.ChangeGameState(stateRequest);
    }

    [ClientRpc]
    void RpcShowRollResults()
    {
        uiManager.UpdateRollText(gameManager.myRoll, gameManager.hisRoll);

    }

    [Command]
    public void CmdDestroyDie()
    {
        Debug.Log("Destroying");
        GameObject dice;
        dice = GameObject.Find("Oct1");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct2");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct3");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct4");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct5");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct6");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct7");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct8");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct1(1)");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct2(1)");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct3(1)");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct4(1)");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct5(1)");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct6(1)");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct7(1)");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
        dice = GameObject.Find("Oct8(1)");
        if (dice != null)
        {
            NetworkServer.Destroy(dice);
        }
    }

}
