using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class StartRoll : NetworkBehaviour
{
    public bool wasClicked = false;
    public PlayerManager playerManager;


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
