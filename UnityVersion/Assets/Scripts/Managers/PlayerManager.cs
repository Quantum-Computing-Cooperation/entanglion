using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using Mirror;
using UnityEngine.UI;




public class PlayerManager : NetworkBehaviour
{

    public class SyncListDice : SyncList<GameObject>{}

    //other managers
    public UIManager uiManager;
    public GameManager gameManager;

    //all cards gameobjects
    public GameObject[] die = new GameObject[8];
    public GameObject[] CentariousDie = new GameObject[2];
    public GameObject Quantumcomponents;
    public GameObject card1;
    public GameObject card2;
    List<GameObject> cards = new List<GameObject>();
    public GameObject detectionRateToken;
    public GameObject blueShip;
    public GameObject redShip;
    public GameObject blueShipInstance;
    public GameObject redShipInstance;

    //Gameobject References
    GameObject dice;
    public SyncListDice dieReferences = new SyncListDice();
    public GameObject engineDeck;

    //zones
    public GameObject player1Area;
    public GameObject player2Area;
    public GameObject dropZone;
    public GameObject dieArea;
    public GameObject otherDieArea;
    public GameObject planetRollArea;
    public GameObject mainCanvas;

    //Buttons
    public GameObject rollButton;
    public GameObject startGameButton;
    public GameObject rollPlanet;

    private void Start()
    {
        blueShipInstance = Instantiate(blueShip, new Vector2(0, 0), Quaternion.identity);
        redShipInstance = Instantiate(redShip, new Vector2(0, 0), Quaternion.identity);
    }
    public override void OnStartClient()
    {
        base.OnStartClient();
        Quantumcomponents = GameObject.Find("Quantum_Components");
        foreach (Transform child in Quantumcomponents.transform) child.gameObject.SetActive(false);
        player1Area = GameObject.Find("Player1Area");
        player2Area = GameObject.Find("Player2Area");
        dropZone = GameObject.Find("DropZone");
        dieArea = GameObject.Find("DieArea");
        otherDieArea = GameObject.Find("OtherDieArea");
        gameManager = GameObject.Find("GameManager").GetComponent<GameManager>();
        uiManager = GameObject.Find("UIManager").GetComponent<UIManager>();
        rollButton = GameObject.Find("RollButton");
        startGameButton = GameObject.Find("StartGameButton");
        detectionRateToken = GameObject.Find("Detection_Rate_Token");
        engineDeck = GameObject.Find("EngineDeck");
        rollPlanet = GameObject.Find("RollPlanet");
        planetRollArea = GameObject.Find("PlanetRollArea");
        gameManager.gameState = "Initialize {}";
        mainCanvas = GameObject.Find("Main_Canvas");
    }

    [Server]
    public override void OnStartServer()
    {
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
        RpcChangeGameState("Compile {}");


        StartCoroutine(WaitForCompile());
    }

    IEnumerator WaitForCompile()
    {
        //yield on a new YieldInstruction that waits for 1 seconds.
        yield return new WaitForSeconds(1);
        if (gameManager.gameState == "Compile {Draw}")
        {
            RpcShowRollResults();
            RpcEnableRollButton();

            //The host needs to cmd destroy die
            RpcDestroyDie();
            RpcChangeGameState("Initialize {}");
        }
        if (gameManager.gameState == "Compile {Higher}" || gameManager.gameState == "Compile {Lower}")
        {
            RpcShowRollResults();
        }
    }

    [ClientRpc]
    void RpcDestroyDie()
    {
        CmdDestroyDie();
    }

    [ClientRpc]
    void RpcChangeTurn()
    {
        gameManager.changeTurn();
    }



    [ClientRpc]
    public void RpcReenableRolling()
    {
        rollButton.GetComponent<StartRoll>().wasClicked = false;
    }

    [Command]
    public void CmdRollPlanet()
    {
        int rand = Random.Range(0, CentariousDie.Length);
        GameObject dice = Instantiate(CentariousDie[rand], new Vector2(0, 0), Quaternion.identity);
        NetworkServer.Spawn(dice, connectionToClient);
        RpcShowCentDie(dice, rand);
        RPCShowShip((rand == 0)? "ZERO": "ONE");
        RpcChangeTurn();
        RpcChangeGameState("Execute {}");
        StartCoroutine(WaitForExecute());
    }

    IEnumerator WaitForExecute()
    {
        //yield on a new YieldInstruction that waits for 1 seconds.
        yield return new WaitForSeconds(1);
        if(gameManager.gameState == "Execute {}")
        {
            CmdStartGame();
        }
        
    }

    [Command]
    void CmdStartGame()
    {

    }

    [ClientRpc]
    void RpcChangeGameState(string state)
    {
        gameManager.ChangeGameState(state);
    }

    [ClientRpc]
    void RpcShowCentDie(GameObject dice, int rand)
    {
        if (hasAuthority)
        {
            dice.transform.SetParent(planetRollArea.transform, false);
        }

    }

    public void PlayCard(GameObject card) => CmdPlayCard(card);

    [Command]
    void CmdPlayCard(GameObject card) => RpcShowCard(card, "Played");

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
    void RPCShowShip(string planet)
    {
        if (hasAuthority)
        {
            blueShipInstance.transform.SetParent(mainCanvas.transform, false);
            blueShipInstance.GetComponent<ShipPlacement>().planet = planet;
        }
        else
        {
            redShipInstance.transform.SetParent(mainCanvas.transform, false);
            redShipInstance.GetComponent<ShipPlacement>().planet = planet;
        }

    }



    [ClientRpc]
    void RpcShowRollResults()
    {
        uiManager.UpdateRollText(gameManager.myRoll, gameManager.hisRoll);
    }
    [Command]
    public void CmdDestroyDie()
    {
        var children = new List<GameObject>();
        foreach (Transform child in dieArea.transform) children.Add(child.gameObject);
        foreach (Transform child in otherDieArea.transform) children.Add(child.gameObject);
        children.ForEach(child => NetworkServer.Destroy(child));
    }
    [Command]
    public void CmdDestroyPlanetDie()
    {
        var children = new List<GameObject>();
        foreach (Transform child in planetRollArea.transform) children.Add(child.gameObject);
        children.ForEach(child => NetworkServer.Destroy(child));
    }

    [ClientRpc]
    void RpcDisplayQc(string[] qcLocations)
    {
        int i = 0;
        foreach (Transform child in Quantumcomponents.transform)
        {
            child.gameObject.SetActive(true);
            child.gameObject.GetComponent<QuantumComponent>().planet = qcLocations[i];
            i++;
        }
    }

    [Command]
    public void CmdSetupGame()
    {
        RpcDisableStartButton();
        //Place the Quantum Components
        gameManager.ShuffleQcPlanets();;
        RpcDisplayQc(gameManager.qcPlanets);
        //Set The initial detection Rate
        RpcChangeDetectionRate(0);
        //Shuffle the Engine Card Stack
        // NOTHING NEEDS TO BE DONE ALL DONE IN START FUNCTION OF OBJECT
        //Prepare the Quantum Event Deck
        //TODO
        //Determine the first player
        RpcEnableRollButton();
        //Determine The initial ship locations
        //NOT HERE
        //Draw Engine Cards
        //NOT HERE
    }

    [ClientRpc]
    void RpcDisableStartButton()
    {
        startGameButton.GetComponent<StartGame>().wasClicked = true;
    }

    [ClientRpc]
    void RpcEnableRollButton()
    {
        rollButton.GetComponent<StartRoll>().wasClicked = false;
    }

    [ClientRpc]
    void RpcChangeDetectionRate(int detectionRate)
    {
        detectionRateToken.GetComponent<DetectionDisplay>().rate = detectionRate;
    }
    

}
