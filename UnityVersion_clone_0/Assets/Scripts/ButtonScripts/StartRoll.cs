using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class StartRoll : NetworkBehaviour
{
    public bool wasClicked;
    public PlayerManager playerManager;
    private void Start()
    {
        wasClicked = true;
    }

    public void OnRoll()
    {
        if (!wasClicked)
        {
            wasClicked = true;
            NetworkIdentity networkIdentity = NetworkClient.connection.identity;
            playerManager = networkIdentity.GetComponent<PlayerManager>();
            playerManager.CmdRollDie();

        }

    }

}
